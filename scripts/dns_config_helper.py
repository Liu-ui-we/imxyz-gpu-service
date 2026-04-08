#!/usr/bin/env python3
"""
DNS配置助手 - 针对imxyz.xyz域名
提供不同注册商的详细配置步骤
"""

import webbrowser
import os
import json
from datetime import datetime

class DNSConfigHelper:
    """DNS配置助手类"""

    def __init__(self):
        self.registrars = {
            "namecheap": {
                "name": "Namecheap",
                "login_url": "https://www.namecheap.com/myaccount/login/",
                "dns_url": "https://ap.www.namecheap.com/Domains/DomainControlPanel",
                "config": {
                    "cname": {
                        "type": "CNAME Record",
                        "host": "@",
                        "value": "liu-ui-we.github.io",
                        "ttl": "Automatic"
                    },
                    "a_records": {
                        "type": "A Records",
                        "records": [
                            {"host": "@", "value": "185.199.108.153", "ttl": "Automatic"},
                            {"host": "@", "value": "185.199.109.153", "ttl": "Automatic"},
                            {"host": "@", "value": "185.199.110.153", "ttl": "Automatic"},
                            {"host": "@", "value": "185.199.111.153", "ttl": "Automatic"}
                        ]
                    }
                }
            },
            "godaddy": {
                "name": "GoDaddy",
                "login_url": "https://sso.godaddy.com/",
                "dns_url": "https://dcc.godaddy.com/manage/imxyz.xyz/dns",
                "config": {
                    "cname": {
                        "type": "CNAME",
                        "name": "@",
                        "data": "liu-ui-we.github.io",
                        "ttl": "600"
                    },
                    "a_records": {
                        "type": "A",
                        "records": [
                            {"name": "@", "data": "185.199.108.153", "ttl": "600"},
                            {"name": "@", "data": "185.199.109.153", "ttl": "600"},
                            {"name": "@", "data": "185.199.110.153", "ttl": "600"},
                            {"name": "@", "data": "185.199.111.153", "ttl": "600"}
                        ]
                    }
                }
            },
            "google": {
                "name": "Google Domains",
                "login_url": "https://domains.google.com/registrar",
                "dns_url": "https://domains.google.com/registrar/imxyz.xyz/dns",
                "config": {
                    "cname": {
                        "type": "CNAME",
                        "hostname": "@",
                        "destination": "liu-ui-we.github.io",
                        "ttl": "3600"
                    },
                    "a_records": {
                        "type": "A",
                        "records": [
                            {"hostname": "@", "ipv4_address": "185.199.108.153"},
                            {"hostname": "@", "ipv4_address": "185.199.109.153"},
                            {"hostname": "@", "ipv4_address": "185.199.110.153"},
                            {"hostname": "@", "ipv4_address": "185.199.111.153"}
                        ]
                    }
                }
            },
            "aliyun": {
                "name": "阿里云万网",
                "login_url": "https://account.aliyun.com/login/login.htm",
                "dns_url": "https://dc.console.aliyun.com/next/index#/domain/list/all-domain",
                "config": {
                    "cname": {
                        "type": "CNAME",
                        "主机记录": "@",
                        "记录值": "liu-ui-we.github.io",
                        "TTL": "600"
                    },
                    "a_records": {
                        "type": "A",
                        "records": [
                            {"主机记录": "@", "记录值": "185.199.108.153", "TTL": "600"},
                            {"主机记录": "@", "记录值": "185.199.109.153", "TTL": "600"},
                            {"主机记录": "@", "记录值": "185.199.110.153", "TTL": "600"},
                            {"主机记录": "@", "记录值": "185.199.111.153", "TTL": "600"}
                        ]
                    }
            }
        }
        }

    def print_header(self, title):
        """打印标题"""
        print("\n" + "="*70)
        print(f"📡 {title}")
        print("="*70)

    def get_registrar_choice(self):
        """获取用户选择的注册商"""
        print("\n请选择你的域名注册商:")
        for i, (key, info) in enumerate(self.registrars.items(), 1):
            print(f"{i}. {info['name']}")
        print(f"{len(self.registrars) + 1}. 其他 (请告诉我具体名称)")

        try:
            choice = int(input("\n请输入数字选择: "))
            if 1 <= choice <= len(self.registrars):
                key = list(self.registrars.keys())[choice - 1]
                return key, self.registrars[key]
            elif choice == len(self.registrars) + 1:
                other = input("请输入你的注册商名称: ").strip()
                return "other", {"name": other, "custom": True}
            else:
                print("❌ 选择无效")
                return None, None
        except ValueError:
            print("❌ 请输入数字")
            return None, None

    def configure_namecheap(self, registrar_info):
        """配置Namecheap DNS"""
        print(f"\n🔧 Namecheap DNS 配置步骤:")
        print("1. 登录: " + registrar_info['login_url'])
        print("2. 进入控制面板 → Domain List → 点击 imxyz.xyz → MANAGE")
        print("3. 选择 'Advanced DNS' 标签页")
        print("4. 删除现有的 A 记录和 CNAME 记录")
        print("5. 添加新的 CNAME 记录:")
        print("   - Host: @")
        print("   - Value: liu-ui-we.github.io")
        print("   - TTL: Automatic")
        print("\n或者添加 A 记录:")
        print("   - Host: @")
        print("   - Value: 185.199.108.153 (TTL: Automatic)")
        print("   - 同样添加其他三个IP地址")

        webbrowser.open(registrar_info['login_url'])

        print("\n✅ 配置完成后，需要等待 2-48 小时 DNS 传播")

        return {
            "action": "cname_or_a_records",
            "details": registrar_info['config']
        }

    def configure_godaddy(self, registrar_info):
        """配置GoDaddy DNS"""
        print(f"\n🔧 GoDaddy DNS 配置步骤:")
        print("1. 登录: " + registrar_info['login_url'])
        print("2. 进入产品页面 → Domains → 点击 imxyz.xyz → DNS")
        print("3. 删除现有的所有记录")
        print("4. 点击 'Add' 按钮")
        print("5. 添加 CNAME 记录:")
        print("   - Type: CNAME")
        print("   - Host: @")
        print("   - Points to: liu-ui-we.github.io")
        print("   - TTL: 600 seconds")

        webbrowser.open(registrar_info['login_url'])

        print("\n✅ 配置完成后，需要等待 2-48 小时 DNS 传播")

        return {
            "action": "cname_or_a_records",
            "details": registrar_info['config']
        }

    def configure_other(self, registrar_info):
        """配置其他注册商DNS"""
        print(f"\n🔧 {registrar_info['name']} DNS 通用配置步骤:")
        print("1. 登录你的注册商控制面板")
        print("2. 找到域名管理 → DNS 管理")
        print("3. 删除现有的所有记录")
        print("\n4. 添加以下记录:")
        print("   选项 A - CNAME 记录:")
        print("   - 类型: CNAME")
        print("   - 主机/名称: @ (或留空)")
        print("   - 值/目标: liu-ui-we.github.io")
        print("   - TTL: 600 或自动")

        print("\n   选项 B - A 记录:")
        print("   添加四条A记录:")
        print("   1. 主机: @, 值: 185.199.108.153")
        print("   2. 主机: @, 值: 185.199.109.153")
        print("   3. 主机: @, 值: 185.199.110.153")
        print("   4. 主机: @, 值: 185.199.111.153")

        print("\n⚠️  CNAME记录更简单，但有些注册商可能不支持根域的CNAME")

        return {
            "action": "configure_dns",
            "details": {
                "recommended": "CNAME记录: @ → liu-ui-we.github.io",
                "alternative": "A记录: 四个特定IP地址"
            }
        }

    def save_configuration(self, registrar_key, registrar_info, config_result):
        """保存DNS配置信息"""
        config = {
            "domain": "imxyz.xyz",
            "registrar": registrar_info['name'],
            "configured_at": datetime.now().isoformat(),
            "target": "liu-ui-we.github.io",
            "a_records": [
                "185.199.108.153",
                "185.199.109.153",
                "185.199.110.153",
                "185.199.111.153"
            ],
            "notes": "DNS配置用于GitHub Pages托管",
            "timestamp": int(datetime.now().timestamp()),
            "config_details": config_result
        }

        config_dir = "/c/Users/31883/Documents/imxyz-gpu-service/config"
        os.makedirs(config_dir, exist_ok=True)

        config_file = os.path.join(config_dir, "dns_config.json")

        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        print(f"\n✅ DNS配置已保存: {config_file}")
        print(f"   域名: imxyz.xyz")
        print(f"   注册商: {registrar_info['name']}")
        print(f"   目标: liu-ui-we.github.io")

        return config_file

    def check_dns_propagation(self):
        """检查DNS传播状态"""
        print("\n🌐 DNS传播检查:")
        print("配置完成后，DNS可能需要 2-48 小时传播到全球")
        print("\n你可以使用以下工具检查:")
        print("1. https://dnschecker.org (搜索 'imxyz.xyz')")
        print("2. https://www.whatsmydns.net")
        print("3. 命令行: nslookup imxyz.xyz")

        print("\n📊 传播状态:")
        print("• 北美: 2-4小时")
        print("• 欧洲: 4-6小时")
        print("• 亚洲: 6-24小时")
        print("• 全球: 最多48小时")

        print("\n🔍 传播成功后，你将能够:")
        print("1. 通过 imxyz.xyz 访问网站")
        print("2. 看到 'Secure' HTTPS 标识 (证书签发后)")
        print("3. 确保所有地区都能访问")

def main():
    """主函数"""
    helper = DNSConfigHelper()

    helper.print_header("imxyz.xyz DNS配置助手")

    print("🎯 目标: 将 imxyz.xyz 指向 GitHub Pages (liu-ui-we.github.io)")

    # 获取注册商信息
    registrar_key, registrar_info = helper.get_registrar_choice()

    if not registrar_key:
        return

    print(f"\n📋 你选择的注册商: {registrar_info['name']}")

    # 根据注册商提供具体步骤
    config_result = None

    if registrar_key == "namecheap":
        config_result = helper.configure_namecheap(registrar_info)
    elif registrar_key == "godaddy":
        config_result = helper.configure_godaddy(registrar_info)
    elif registrar_key == "other":
        config_result = helper.configure_other(registrar_info)
    else:
        print(f"\n⚠️  暂未提供 {registrar_info['name']} 的详细配置步骤")
        print("  请登录你的注册商控制面板，参考以下通用步骤:")
        config_result = helper.configure_other(registrar_info)

    # 保存配置
    if config_result:
        config_file = helper.save_configuration(registrar_key, registrar_info, config_result)

    # 传播检查
    helper.check_dns_propagation()

    print("\n🎉 DNS配置指导完成!")
    print("请按照上述步骤在你的注册商控制面板中配置DNS记录")
    print("配置完成后，预计2-48小时内 imxyz.xyz 将指向你的网站")

if __name__ == "__main__":
    main()