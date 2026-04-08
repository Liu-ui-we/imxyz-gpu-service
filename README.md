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

### 5. Test the System
```bash
# Generate SSH key for instances
python cloud_manager.py genkey

# List available instances (after configuring credentials)
python cloud_manager.py list --provider aliyun
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

## 🤝 Support & Community

### Getting Help
- **Discord**: Join our community
- **Email**: hello@imxyz.xyz
- **GitHub Issues**: Report bugs or request features

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