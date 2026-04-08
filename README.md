# imxyz.xyz - GPU Compute Service from China

A turnkey solution for reselling affordable GPU compute from Chinese cloud providers to international customers. Earn 20-30% margins by leveraging China's lower cloud costs.

![imxyz.xyz Screenshot](public/images/screenshot.png)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/imxyz-gpu-service.git
cd imxyz-gpu-service
```

### 2. Set Up Website
The website is ready to deploy. You can:
- **Deploy to GitHub Pages** (free): See [Deployment Guide](#deployment)
- **Deploy to Vercel/Netlify** (free)
- **Host on any static web server**

### 3. Configure Cloud Access
```bash
# Copy example config
cp config/cloud_config.ini.example config/cloud_config.ini

# Edit with your credentials
nano config/cloud_config.ini
```

### 4. Install Python Dependencies
```bash
cd scripts
pip install -r requirements.txt
```

### 5. One-Click Quick Start
```bash
# Run the quick start wizard (recommended for beginners)
python quickstart.py

# Or run individual setup scripts:
# 1. Configure Formspree form
python scripts/formspree_setup.py

# 2. Configure DNS for imxyz.xyz
python scripts/dns_config_helper.py

# 3. Check deployment status
python scripts/deployment_check.py
```

### 6. Test the System
```bash
# Generate SSH key for instances
python scripts/cloud_manager.py genkey

# List available instances (after configuring credentials)
python scripts/cloud_manager.py list --provider aliyun
```

## 📋 Features

### ✅ Complete Website
- Modern, responsive design
- Pricing comparison tables
- Order form (with Formspree integration)
- FAQ section
- Mobile-friendly navigation

### ✅ Automation Scripts
- **Cloud Instance Management**: Create, list, delete GPU instances
- **Multi-provider Support**: Aliyun, Tencent Cloud, Huawei Cloud
- **Cost Estimation**: Calculate pricing with your markup
- **SSH Key Management**: Automatic key generation
- **Logging**: Comprehensive activity logs

### ✅ Business Tools
- **Configuration Management**: Centralized settings
- **Customer Database**: SQLite/PostgreSQL support
- **Email Notifications**: Automated customer communication
- **Payment Integration**: PayPal & Stripe ready
- **Monitoring**: Instance health checks

## 🏗️ Architecture

```
imxyz.xyz/
├── public/                    # Website files
│   ├── index.html            # Main landing page
│   ├── css/                  # Stylesheets
│   ├── js/                   # JavaScript
│   └── images/               # Graphics & screenshots
├── scripts/                  # Automation scripts
│   ├── cloud_manager.py      # Main cloud management
│   ├── requirements.txt      # Python dependencies
│   └── order_processor.py    # (Optional) Order automation
├── config/                   # Configuration
│   ├── cloud_config.ini.example
│   └── cloud_config.ini      # Your actual config
├── docs/                     # Documentation
├── logs/                     # Application logs
└── ssh_keys/                 # SSH key pairs
```

## 🔧 Configuration

### 1. Cloud Provider Setup

#### Alibaba Cloud (Aliyun)
1. Register at [aliyun.com](https://www.aliyun.com)
2. Go to RAM Console: https://ram.console.aliyun.com/users
3. Create a user with **Programmatic Access**
4. Grant `AliyunECSFullAccess` permission
5. Copy AccessKey ID and Secret to config

#### Tencent Cloud
1. Register at [cloud.tencent.com](https://cloud.tencent.com)
2. Go to API Key Management: https://console.cloud.tencent.com/cam/capi
3. Create a SecretId and SecretKey
4. Grant `CVM_FullAccess` permission

### 2. Website Configuration

Edit `public/index.html`:
- Update contact information (Discord, email)
- Modify pricing tables (lines 120-150)
- Update Formspree form ID (line 165)
- Customize colors in `public/css/style.css`

### 3. Payment Setup

#### Formspree (Free Tier)
1. Sign up at [formspree.io](https://formspree.io)
2. Create a new form
3. Replace form action URL in `index.html` (line 165)

#### PayPal/Stripe (For Payments)
1. Set up PayPal Business account
2. Get API credentials from PayPal Developer
3. Update `config/cloud_config.ini` with credentials

## 💰 Pricing Strategy

### Example Calculation
```
Aliyun V100 GPU instance: $3.50/hour
Your markup (20%): $0.70/hour
Your price: $4.20/hour

AWS equivalent: $4.10/hour
Your advantage: Same price, better margin
```

### Recommended Pricing
| GPU Type | Cost (China) | Your Price | AWS Price | Savings |
|----------|--------------|------------|-----------|---------|
| V100 16GB | $3.50/hr | $4.20/hr | $4.10/hr | -$0.10 |
| A100 40GB | $8.20/hr | $9.84/hr | $12.50/hr | $2.66 |
| CPU Only | $0.42/hr | $0.50/hr | $0.68/hr | $0.18 |

**Strategy**: Match or slightly undercut AWS for V100, offer significant savings on A100.

## 🛠️ Usage

### Manual Process (Recommended for Start)
1. Customer submits form on website
2. You receive email notification
3. Manually create instance:
   ```bash
   python cloud_manager.py create \
     --name "customer-project-001" \
     --type "ecs.gn6i-c8g1.2xlarge" \
     --hours 24
   ```
4. Send SSH credentials to customer
5. Monitor usage and invoice

### Semi-Automated Process
1. Customer submits form
2. Script automatically creates instance
3. Automated email with credentials
4. Automated monitoring and alerts

### Full Automation (Advanced)
- Integrate with payment gateway
- Automatic instance provisioning
- Usage-based billing
- Customer dashboard

## 📈 Marketing & Customer Acquisition

### Initial Launch
1. **Reddit Communities**:
   - r/MachineLearning
   - r/deeplearning
   - r/learnmachinelearning
   - r/SideProject

2. **Discord Servers**:
   - FastAI
   - PyTorch
   - TensorFlow
   - AI/ML communities

3. **Content Marketing**:
   - Blog post: "How to get GPU compute for 50% less"
   - Tutorial: "Setting up imxyz.xyz GPU instance"
   - Comparison: "AWS vs China Cloud pricing"

### Growth Strategies
1. **Referral Program**: 10% discount for referrals
2. **Student Discount**: 15% off for .edu emails
3. **Open Source Support**: Free credits for OSS projects
4. **Partnerships**: Collaborate with AI tool platforms

## 🚨 Risk Management

### Technical Risks
- **Network Latency**: 150-250ms from US/EU (manage expectations)
- **Instance Availability**: Some GPU types may be scarce
- **API Rate Limits**: Cloud providers may throttle requests

### Business Risks
- **Currency Fluctuation**: USD/CNY exchange rate changes
- **Regulatory Changes**: China may restrict cloud exports
- **Competition**: Other resellers may enter market

### Mitigation Strategies
1. **Diversify Providers**: Use multiple cloud providers
2. **Clear Communication**: Set proper expectations
3. **Terms of Service**: Include liability limitations
4. **Insurance**: Consider business insurance as you grow

## 📊 Monitoring & Analytics

### Built-in Tools
```bash
# Check instance status
python cloud_manager.py list --provider aliyun

# Monitor costs
python scripts/cost_tracker.py --days 7

# Check logs
tail -f logs/cloud_manager.log
```

### Recommended Third-party Tools
- **UptimeRobot**: Free website monitoring
- **Google Analytics**: Traffic analytics
- **Stripe/PayPal Analytics**: Revenue tracking
- **Discord Webhooks**: Real-time notifications

## 🔒 Security Best Practices

### Instance Security
1. **SSH Key Authentication Only** (disable passwords)
2. **Firewall Rules**: Only allow necessary ports
3. **Regular Updates**: Keep OS and drivers updated
4. **Isolation**: Separate instances for each customer

### Data Security
1. **No Data Storage**: Don't store customer data
2. **Encryption Recommendations**: Guide customers to encrypt sensitive data
3. **Regular Backups**: Backup your configuration and scripts

### Business Security
1. **Separate Accounts**: Use different cloud accounts for business vs personal
2. **API Key Rotation**: Rotate keys every 90 days
3. **Access Control**: Limit who has access to management scripts

## 🌐 Deployment Options

### Option 1: GitHub Pages (Free)
```bash
# Create new repository
# Push website files to main branch
# Enable GitHub Pages in settings
```

### Option 2: Vercel (Free)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

### Option 3: Traditional Hosting
Upload `public/` folder to any web host (Bluehost, HostGator, etc.)

## 🤖 自动化部署脚本

### 🚀 一键快速启动
```bash
# 运行快速启动向导（推荐初学者）
python quickstart.py
```
**功能**：引导式完成所有配置，包含：
- 检查系统环境（Python、Git）
- 配置Formspree订单表单
- 设置DNS记录
- 测试网站访问
- 配置云服务API
- 生成启动报告

### 📡 DNS配置助手
```bash
# 针对不同注册商的详细DNS配置指导
python scripts/dns_config_helper.py
```
**支持的注册商**：
- Namecheap
- GoDaddy  
- Google Domains
- 阿里云万网
- 其他注册商通用指导

### 📝 Formspree自动配置
```bash
# 自动化Formspree注册和表单配置
python scripts/formspree_setup.py
```
**功能**：
- 打开Formspree注册页面
- 指导创建“GPU Instance Request”表单
- 自动更新网站代码中的表单ID
- 保存配置记录

### 🔍 部署状态检查
```bash
# 检查所有配置项的完成状态
python scripts/deployment_check.py
```
**检查的项目**：
- GitHub Pages 可访问性
- 项目结构完整性
- Formspree 表单配置
- DNS 记录配置
- 云服务 API 配置
- 生成详细部署报告

### ☁️ 云实例管理（核心功能）
```bash
# 生成SSH密钥
python scripts/cloud_manager.py genkey

# 创建GPU实例
python scripts/cloud_manager.py create --name "客户项目" --type "V100" --hours 24

# 列出所有实例
python scripts/cloud_manager.py list --provider aliyun

# 删除实例
python scripts/cloud_manager.py delete [实例ID]

# 成本估算
python scripts/cloud_manager.py estimate --provider aliyun --type V100 --hours 100
```

### 🧪 测试你的配置
```bash
# 1. 运行完整部署检查
python scripts/deployment_check.py

# 2. 测试Formspree表单
curl -X POST https://formspree.io/f/YOUR_FORM_ID \
  -d "name=Test&email=test@example.com&useCase=AI_Training"

# 3. 测试网站访问
curl -I https://imxyz.xyz
```

## 🤝 获取支持

### 遇到问题？
1. **检查部署报告**：`python scripts/deployment_check.py`
2. **查看详细文档**：`docs/DEPLOYMENT.md`
3. **运行快速启动**：`python quickstart.py`

### 社区支持
- **Discord**: 加入我们的技术社区
- **GitHub Issues**: 报告问题或请求功能
- **Email**: hello@imxyz.xyz (业务咨询)

### Contributing
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Chinese cloud providers for affordable GPU compute
- Open source community for tools and libraries
- Early customers for feedback and support

## 🚀 Next Steps

1. **Week 1**: Deploy website, configure one cloud provider
2. **Week 2**: Get first 3 paying customers (friends/network)
3. **Week 3**: Refine process based on feedback
4. **Month 2**: Add automation for instance creation
5. **Month 3**: Integrate payment processing
6. **Month 6**: Scale to 20+ customers, consider team expansion

---

**Remember**: Start small, validate with real customers, and scale gradually. Your first goal is $100/month, not $10,000/month.

Good luck with your imxyz.xyz journey! 🚀