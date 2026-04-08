#!/usr/bin/env python3
"""
Cloud Instance Manager for imxyz.xyz
Automates creation and management of GPU instances on Chinese cloud providers.
Supports Alibaba Cloud (Aliyun), Tencent Cloud, and Huawei Cloud.
"""

import os
import sys
import json
import time
import argparse
import subprocess
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import configparser

# Try to import cloud SDKs
try:
    import aliyunsdkcore
    import aliyunsdkecs
    from aliyunsdkcore.client import AcsClient
    from aliyunsdkcore.auth.credentials import AccessKeyCredential
    from aliyunsdkecs.request.v20140526 import (
        CreateInstanceRequest,
        DescribeInstancesRequest,
        StartInstanceRequest,
        StopInstanceRequest,
        DeleteInstanceRequest,
        AllocatePublicIpAddressRequest
    )
    ALIYUN_AVAILABLE = True
except ImportError:
    ALIYUN_AVAILABLE = False
    print("Warning: Aliyun SDK not installed. Run: pip install aliyun-python-sdk-core aliyun-python-sdk-ecs")

try:
    import tencentcloud
    from tencentcloud.common import credential
    from tencentcloud.cvm.v20170312 import cvm_client, models
    TENCENT_AVAILABLE = True
except ImportError:
    TENCENT_AVAILABLE = False
    print("Warning: Tencent Cloud SDK not installed. Run: pip install tencentcloud-sdk-python")

# Configuration
CONFIG_FILE = "config/cloud_config.ini"
LOG_FILE = "logs/cloud_manager.log"

class CloudManager:
    """Manages cloud instances across multiple providers."""

    def __init__(self, config_path: str = CONFIG_FILE):
        self.config_path = config_path
        self.config = self.load_config()
        self.clients = self.init_clients()
        self.setup_logging()

    def load_config(self) -> configparser.ConfigParser:
        """Load configuration from INI file."""
        config = configparser.ConfigParser()

        # Default configuration
        config['DEFAULT'] = {
            'default_provider': 'aliyun',
            'default_region': 'cn-hangzhou',
            'default_instance_type': 'ecs.gn6i-c8g1.2xlarge',
            'default_image_id': 'centos_7_9_x64_20G_alibase_20230920.vhd',
            'default_security_group': 'sg-xxx',
            'default_vswitch_id': 'vsw-xxx',
            'billing_method': 'PostPaid',  # PostPaid or PrePaid
            'period': '1',  # For PrePaid, in months
            'auto_release_time': '24',  # Hours before auto release (for temporary instances)
        }

        # Provider-specific sections
        config['aliyun'] = {
            'access_key_id': 'YOUR_ACCESS_KEY',
            'access_key_secret': 'YOUR_SECRET_KEY',
            'regions': 'cn-hangzhou,cn-beijing,cn-shanghai,cn-shenzhen'
        }

        config['tencent'] = {
            'secret_id': 'YOUR_SECRET_ID',
            'secret_key': 'YOUR_SECRET_KEY',
            'regions': 'ap-beijing,ap-shanghai,ap-guangzhou'
        }

        # Try to load actual config
        if os.path.exists(config_path):
            config.read(config_path)
            print(f"Loaded configuration from {config_path}")
        else:
            print(f"Config file {config_path} not found. Using defaults.")
            # Create config directory if it doesn't exist
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            with open(config_path, 'w') as f:
                config.write(f)
            print(f"Created default config file at {config_path}")
            print("Please edit it with your actual API credentials.")

        return config

    def init_clients(self) -> Dict:
        """Initialize cloud provider clients."""
        clients = {}

        # Initialize Aliyun client if available
        if ALIYUN_AVAILABLE and self.config.has_section('aliyun'):
            access_key = self.config.get('aliyun', 'access_key_id')
            secret_key = self.config.get('aliyun', 'access_key_secret')
            region = self.config.get('DEFAULT', 'default_region')

            if access_key != 'YOUR_ACCESS_KEY' and secret_key != 'YOUR_SECRET_KEY':
                credentials = AccessKeyCredential(access_key, secret_key)
                clients['aliyun'] = AcsClient(region_id=region, credential=credentials)
                print("Aliyun client initialized")
            else:
                print("Aliyun credentials not configured")

        # Initialize Tencent Cloud client if available
        if TENCENT_AVAILABLE and self.config.has_section('tencent'):
            secret_id = self.config.get('tencent', 'secret_id')
            secret_key = self.config.get('tencent', 'secret_key')

            if secret_id != 'YOUR_SECRET_ID' and secret_key != 'YOUR_SECRET_KEY':
                cred = credential.Credential(secret_id, secret_key)
                clients['tencent'] = cvm_client.CvmClient(cred, "ap-beijing")
                print("Tencent Cloud client initialized")
            else:
                print("Tencent Cloud credentials not configured")

        return clients

    def setup_logging(self):
        """Setup basic logging."""
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

    def log(self, message: str, level: str = "INFO"):
        """Log a message."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}\n"

        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)

        print(f"{level}: {message}")

    def create_instance(self, provider: str = None, **kwargs) -> Optional[Dict]:
        """Create a new cloud instance."""
        if not provider:
            provider = self.config.get('DEFAULT', 'default_provider')

        if provider == 'aliyun' and 'aliyun' in self.clients:
            return self.create_aliyun_instance(**kwargs)
        elif provider == 'tencent' and 'tencent' in self.clients:
            return self.create_tencent_instance(**kwargs)
        else:
            self.log(f"Unsupported provider or client not initialized: {provider}", "ERROR")
            return None

    def create_aliyun_instance(self, **kwargs) -> Optional[Dict]:
        """Create an Aliyun ECS instance."""
        try:
            client = self.clients['aliyun']

            # Build request
            request = CreateInstanceRequest.CreateInstanceRequest()

            # Set parameters with defaults from config
            region = kwargs.get('region', self.config.get('DEFAULT', 'default_region'))
            instance_type = kwargs.get('instance_type', self.config.get('DEFAULT', 'default_instance_type'))
            image_id = kwargs.get('image_id', self.config.get('DEFAULT', 'default_image_id'))
            security_group = kwargs.get('security_group', self.config.get('DEFAULT', 'default_security_group'))
            vswitch_id = kwargs.get('vswitch_id', self.config.get('DEFAULT', 'default_vswitch_id'))

            request.set_RegionId(region)
            request.set_InstanceType(instance_type)
            request.set_ImageId(image_id)
            request.set_SecurityGroupId(security_group)
            request.set_VSwitchId(vswitch_id)

            # Set optional parameters
            if 'instance_name' in kwargs:
                request.set_InstanceName(kwargs['instance_name'])

            if 'password' in kwargs:
                request.set_Password(kwargs['password'])

            # Billing
            billing_method = kwargs.get('billing_method', self.config.get('DEFAULT', 'billing_method'))
            request.set_InstanceChargeType(billing_method)

            if billing_method == 'PrePaid':
                period = kwargs.get('period', self.config.get('DEFAULT', 'period'))
                request.set_Period(period)
                request.set_PeriodUnit('Month')

            # Make API call
            response = client.do_action_with_exception(request)
            result = json.loads(response.decode('utf-8'))

            instance_id = result.get('InstanceId')

            if instance_id:
                # Allocate public IP
                ip_request = AllocatePublicIpAddressRequest.AllocatePublicIpAddressRequest()
                ip_request.set_InstanceId(instance_id)
                ip_response = client.do_action_with_exception(ip_request)
                ip_result = json.loads(ip_response.decode('utf-8'))

                # Start instance
                start_request = StartInstanceRequest.StartInstanceRequest()
                start_request.set_InstanceId(instance_id)
                start_response = client.do_action_with_exception(start_request)

                self.log(f"Created Aliyun instance: {instance_id}")

                # Return instance info
                return {
                    'provider': 'aliyun',
                    'instance_id': instance_id,
                    'region': region,
                    'instance_type': instance_type,
                    'status': 'Starting',
                    'created_at': datetime.now().isoformat()
                }

        except Exception as e:
            self.log(f"Failed to create Aliyun instance: {e}", "ERROR")
            return None

    def create_tencent_instance(self, **kwargs) -> Optional[Dict]:
        """Create a Tencent Cloud CVM instance."""
        try:
            client = self.clients['tencent']

            # Build request
            request = models.RunInstancesRequest()

            # Set parameters
            params = {
                'Placement': {
                    'Zone': kwargs.get('zone', 'ap-beijing-3')
                },
                'InstanceType': kwargs.get('instance_type', 'S5.MEDIUM8'),
                'ImageId': kwargs.get('image_id', 'img-xxx'),
                'InstanceChargeType': kwargs.get('billing_method', 'POSTPAID_BY_HOUR'),
                'InstanceName': kwargs.get('instance_name', 'imxyz-gpu-instance'),
                'SecurityGroupIds': [kwargs.get('security_group', 'sg-xxx')],
                'VirtualPrivateCloud': {
                    'VpcId': kwargs.get('vpc_id', 'vpc-xxx'),
                    'SubnetId': kwargs.get('subnet_id', 'subnet-xxx')
                }
            }

            # For GPU instances
            if 'gpu_type' in kwargs:
                params['GPU'] = {
                    'GPUType': kwargs.get('gpu_type', 'V100'),
                    'GPUCount': kwargs.get('gpu_count', 1)
                }

            request.from_json_string(json.dumps(params))

            # Make API call
            response = client.RunInstances(request)
            result = json.loads(response.to_json_string())

            instance_ids = result.get('InstanceIdSet', [])

            if instance_ids:
                instance_id = instance_ids[0]
                self.log(f"Created Tencent Cloud instance: {instance_id}")

                return {
                    'provider': 'tencent',
                    'instance_id': instance_id,
                    'zone': params['Placement']['Zone'],
                    'instance_type': params['InstanceType'],
                    'status': 'Pending',
                    'created_at': datetime.now().isoformat()
                }

        except Exception as e:
            self.log(f"Failed to create Tencent Cloud instance: {e}", "ERROR")
            return None

    def list_instances(self, provider: str = None) -> List[Dict]:
        """List all instances for a provider."""
        instances = []

        if not provider:
            provider = self.config.get('DEFAULT', 'default_provider')

        if provider == 'aliyun' and 'aliyun' in self.clients:
            instances = self.list_aliyun_instances()
        elif provider == 'tencent' and 'tencent' in self.clients:
            instances = self.list_tencent_instances()

        return instances

    def list_aliyun_instances(self) -> List[Dict]:
        """List Aliyun ECS instances."""
        instances = []

        try:
            client = self.clients['aliyun']
            request = DescribeInstancesRequest.DescribeInstancesRequest()
            request.set_PageSize(100)

            response = client.do_action_with_exception(request)
            result = json.loads(response.decode('utf-8'))

            for instance in result.get('Instances', {}).get('Instance', []):
                instances.append({
                    'instance_id': instance.get('InstanceId'),
                    'instance_name': instance.get('InstanceName'),
                    'status': instance.get('Status'),
                    'instance_type': instance.get('InstanceType'),
                    'public_ip': instance.get('PublicIpAddress', {}).get('IpAddress', [])[0] if instance.get('PublicIpAddress', {}).get('IpAddress') else None,
                    'private_ip': instance.get('InnerIpAddress', {}).get('IpAddress', [])[0] if instance.get('InnerIpAddress', {}).get('IpAddress') else None,
                    'region': instance.get('RegionId'),
                    'created_at': instance.get('CreationTime')
                })

        except Exception as e:
            self.log(f"Failed to list Aliyun instances: {e}", "ERROR")

        return instances

    def list_tencent_instances(self) -> List[Dict]:
        """List Tencent Cloud CVM instances."""
        instances = []

        try:
            client = self.clients['tencent']
            request = models.DescribeInstancesRequest()
            request.Limit = 100

            response = client.DescribeInstances(request)
            result = json.loads(response.to_json_string())

            for instance in result.get('InstanceSet', []):
                instances.append({
                    'instance_id': instance.get('InstanceId'),
                    'instance_name': instance.get('InstanceName'),
                    'status': instance.get('InstanceState'),
                    'instance_type': instance.get('InstanceType'),
                    'public_ip': instance.get('PublicIpAddresses', [])[0] if instance.get('PublicIpAddresses') else None,
                    'private_ip': instance.get('PrivateIpAddresses', [])[0] if instance.get('PrivateIpAddresses') else None,
                    'zone': instance.get('Placement', {}).get('Zone'),
                    'created_at': instance.get('CreatedTime')
                })

        except Exception as e:
            self.log(f"Failed to list Tencent instances: {e}", "ERROR")

        return instances

    def delete_instance(self, instance_id: str, provider: str = None) -> bool:
        """Delete a cloud instance."""
        if not provider:
            provider = self.config.get('DEFAULT', 'default_provider')

        if provider == 'aliyun' and 'aliyun' in self.clients:
            return self.delete_aliyun_instance(instance_id)
        elif provider == 'tencent' and 'tencent' in self.clients:
            return self.delete_tencent_instance(instance_id)
        else:
            self.log(f"Unsupported provider: {provider}", "ERROR")
            return False

    def delete_aliyun_instance(self, instance_id: str) -> bool:
        """Delete an Aliyun ECS instance."""
        try:
            client = self.clients['aliyun']
            request = DeleteInstanceRequest.DeleteInstanceRequest()
            request.set_InstanceId(instance_id)

            response = client.do_action_with_exception(request)
            self.log(f"Deleted Aliyun instance: {instance_id}")
            return True

        except Exception as e:
            self.log(f"Failed to delete Aliyun instance {instance_id}: {e}", "ERROR")
            return False

    def delete_tencent_instance(self, instance_id: str) -> bool:
        """Delete a Tencent Cloud CVM instance."""
        try:
            client = self.clients['tencent']
            request = models.TerminateInstancesRequest()
            request.InstanceIds = [instance_id]

            response = client.TerminateInstances(request)
            self.log(f"Deleted Tencent Cloud instance: {instance_id}")
            return True

        except Exception as e:
            self.log(f"Failed to delete Tencent instance {instance_id}: {e}", "ERROR")
            return False

    def generate_ssh_key(self, key_name: str = "imxyz_gpu_key") -> Tuple[bool, str]:
        """Generate an SSH key pair for instance access."""
        try:
            private_key_path = f"ssh_keys/{key_name}"
            public_key_path = f"{private_key_path}.pub"

            os.makedirs("ssh_keys", exist_ok=True)

            # Generate key pair using ssh-keygen
            subprocess.run([
                'ssh-keygen', '-t', 'rsa', '-b', '4096',
                '-f', private_key_path,
                '-N', '',  # No passphrase for automation
                '-C', f"imxyz-gpu-{datetime.now().strftime('%Y%m%d')}"
            ], check=True, capture_output=True)

            # Read public key
            with open(public_key_path, 'r') as f:
                public_key = f.read().strip()

            self.log(f"Generated SSH key pair: {private_key_path}")
            return True, public_key

        except Exception as e:
            self.log(f"Failed to generate SSH key: {e}", "ERROR")
            return False, ""

    def estimate_cost(self, provider: str, instance_type: str, hours: int) -> float:
        """Estimate cost for running an instance."""
        # Simple cost estimation based on known prices
        # In production, you would query the cloud provider's pricing API

        pricing = {
            'aliyun': {
                'ecs.gn6i-c8g1.2xlarge': 3.5,  # $/hour (V100 GPU)
                'ecs.gn7i-c16g1.4xlarge': 8.2,  # $/hour (A100 GPU)
                'ecs.g6e.large': 0.42,  # $/hour (CPU only)
            },
            'tencent': {
                'GI1.8XLARGE64': 4.8,  # $/hour (V100)
                'GI2.8XLARGE64': 9.5,  # $/hour (A100)
                'S5.MEDIUM8': 0.48,  # $/hour (CPU)
            }
        }

        if provider in pricing and instance_type in pricing[provider]:
            hourly_rate = pricing[provider][instance_type]
            return hourly_rate * hours
        else:
            # Default estimate
            return 3.5 * hours  # Conservative default

def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Cloud Instance Manager for imxyz.xyz')
    parser.add_argument('--config', default=CONFIG_FILE, help='Path to config file')

    subparsers = parser.add_subparsers(dest='command', help='Command to execute')

    # Create instance command
    create_parser = subparsers.add_parser('create', help='Create a new instance')
    create_parser.add_argument('--provider', choices=['aliyun', 'tencent'], help='Cloud provider')
    create_parser.add_argument('--name', help='Instance name')
    create_parser.add_argument('--type', help='Instance type')
    create_parser.add_argument('--hours', type=int, default=24, help='Duration in hours')

    # List instances command
    list_parser = subparsers.add_parser('list', help='List instances')
    list_parser.add_argument('--provider', choices=['aliyun', 'tencent'], help='Cloud provider')

    # Delete instance command
    delete_parser = subparsers.add_parser('delete', help='Delete an instance')
    delete_parser.add_argument('instance_id', help='Instance ID to delete')
    delete_parser.add_argument('--provider', choices=['aliyun', 'tencent'], help='Cloud provider')

    # Generate SSH key command
    key_parser = subparsers.add_parser('genkey', help='Generate SSH key pair')
    key_parser.add_argument('--name', default='imxyz_gpu_key', help='Key name')

    # Estimate cost command
    cost_parser = subparsers.add_parser('estimate', help='Estimate cost')
    cost_parser.add_argument('--provider', required=True, choices=['aliyun', 'tencent'])
    cost_parser.add_argument('--type', required=True, help='Instance type')
    cost_parser.add_argument('--hours', type=int, required=True, help='Duration in hours')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    # Initialize cloud manager
    manager = CloudManager(args.config)

    if args.command == 'create':
        instance = manager.create_instance(
            provider=args.provider,
            instance_name=args.name,
            instance_type=args.type
        )

        if instance:
            print(json.dumps(instance, indent=2))
            cost = manager.estimate_cost(
                instance['provider'],
                instance['instance_type'],
                args.hours
            )
            print(f"\nEstimated cost for {args.hours} hours: ${cost:.2f}")
        else:
            print("Failed to create instance")
            sys.exit(1)

    elif args.command == 'list':
        instances = manager.list_instances(args.provider)

        if instances:
            for i, instance in enumerate(instances, 1):
                print(f"{i}. {instance['instance_name']} ({instance['instance_id']})")
                print(f"   Status: {instance['status']}")
                print(f"   Type: {instance['instance_type']}")
                print(f"   Public IP: {instance['public_ip'] or 'N/A'}")
                print(f"   Created: {instance['created_at']}")
                print()
        else:
            print("No instances found or failed to list instances")

    elif args.command == 'delete':
        success = manager.delete_instance(args.instance_id, args.provider)

        if success:
            print(f"Successfully deleted instance: {args.instance_id}")
        else:
            print(f"Failed to delete instance: {args.instance_id}")
            sys.exit(1)

    elif args.command == 'genkey':
        success, public_key = manager.generate_ssh_key(args.name)

        if success:
            print(f"Generated SSH key: ssh_keys/{args.name}")
            print(f"\nPublic key:\n{public_key}")
        else:
            print("Failed to generate SSH key")
            sys.exit(1)

    elif args.command == 'estimate':
        cost = manager.estimate_cost(args.provider, args.type, args.hours)
        print(f"Estimated cost for {args.hours} hours: ${cost:.2f}")

if __name__ == '__main__':
    main()