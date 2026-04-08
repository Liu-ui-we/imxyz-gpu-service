# Deployment Guide for imxyz.xyz

This guide walks you through deploying your GPU compute service website and automation scripts.

## Prerequisites

- GitHub account (for free hosting)
- Cloud provider account (Aliyun/Tencent Cloud)
- Python 3.8+ (for automation scripts)
- Basic command line knowledge

## Option 1: GitHub Pages (Recommended for Start)

### Step 1: Create GitHub Repository
1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name: `imxyz-gpu-service`
4. Description: "GPU compute service from China"
5. Choose **Public**
6. Click "Create repository"

### Step 2: Upload Website Files
```bash
# Clone your repository
git clone https://github.com/YOUR_USERNAME/imxyz-gpu-service.git
cd imxyz-gpu-service

# Copy website files to the repository root
# (Assuming you're in the project directory)
cp -r public/* .

# Or if you already have the imxyz-gpu-service folder:
# Just ensure index.html, css/, js/, images/ are in root
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" → "Pages"
3. Under "Source", select:
   - Branch: `main`
   - Folder: `/` (root)
4. Click "Save"
5. Wait 1-2 minutes for deployment
6. Your site will be at: `https://YOUR_USERNAME.github.io/imxyz-gpu-service`

### Step 4: Set Custom Domain (Optional)
1. Buy domain from Namecheap/GoDaddy ($10-15/year)
2. In GitHub Pages settings, add custom domain: `imxyz.xyz`
3. Update DNS records at your domain registrar:
   ```
   Type: A
   Name: @
   Value: 185.199.108.153
   Value: 185.199.109.153
   Value: 185.199.110.153
   Value: 185.199.111.153
   ```

## Option 2: Vercel (Alternative Free Hosting)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Deploy
```bash
# Navigate to website directory
cd imxyz-gpu-service/public

# Deploy
vercel

# Follow prompts:
# - Set project name: imxyz-gpu-service
# - No framework (static site)
# - Output directory: . (current)

# For production:
vercel --prod
```

### Step 3: Set Environment Variables (Optional)
In Vercel dashboard → Project Settings → Environment Variables:
- `FORMSPREE_FORM_ID`: Your Formspree form ID
- `PAYPAL_CLIENT_ID`: For payment integration

## Option 3: Traditional Web Hosting

### Step 1: Choose a Host
Recommended for beginners:
- **Bluehost**: $2.95/month (shared hosting)
- **HostGator**: $2.75/month (shared hosting)
- **DigitalOcean**: $6/month (VPS, more control)

### Step 2: Upload Files
1. Login to hosting control panel (cPanel)
2. Go to "File Manager"
3. Upload all files from `public/` folder to `public_html/`
4. Ensure `index.html` is in the root

### Step 3: Configure Domain
1. Point your domain to hosting nameservers
2. Wait 24-48 hours for DNS propagation

## Setting Up Automation Scripts

### Step 1: Install Python Dependencies
```bash
cd scripts
pip install -r requirements.txt
```

### Step 2: Configure Cloud Access
```bash
# Copy example config
cp config/cloud_config.ini.example config/cloud_config.ini

# Edit configuration
nano config/cloud_config.ini

# Fill in:
# - Cloud provider credentials
# - Instance types and pricing
# - Your markup percentage
```

### Step 3: Test the System
```bash
# Generate SSH key
python cloud_manager.py genkey

# Test instance creation (use --dry-run first)
python cloud_manager.py create --name "test-instance" --type "ecs.gn6i-c8g1.2xlarge" --hours 1 --dry-run

# List instances
python cloud_manager.py list --provider aliyun
```

## Email Setup (Formspree)

### Step 1: Create Formspree Account
1. Go to [formspree.io](https://formspree.io)
2. Sign up with GitHub/Google/Email
3. Verify your email address

### Step 2: Create Form
1. Click "New Form"
2. Form name: "GPU Instance Request"
3. Email: your email address
4. Click "Create"

### Step 3: Update Website
1. Copy your form ID (e.g., `xqknvqgw`)
2. Edit `index.html`, line ~165:
   ```html
   <form id="orderForm" action="https://formspree.io/f/xqknvqgw" method="POST">
   ```
3. Replace with your form ID

## Payment Integration

### Option A: PayPal (Easiest)
1. Create PayPal Business account
2. Get API credentials from [PayPal Developer](https://developer.paypal.com)
3. Update config file:
   ```ini
   [payment]
   paypal_client_id = YOUR_CLIENT_ID
   paypal_client_secret = YOUR_SECRET
   ```
4. Add PayPal button to website (optional)

### Option B: Stripe (More Professional)
1. Sign up at [stripe.com](https://stripe.com)
2. Get API keys from Dashboard
3. Update config file:
   ```ini
   [payment]
   stripe_api_key = sk_live_xxxx
   ```
4. Consider using [Payment Links](https://stripe.com/payments/payment-links) for simple integration

## Monitoring Setup

### Website Uptime
- **UptimeRobot**: Free 50 monitors
  1. Sign up at [uptimerobot.com](https://uptimerobot.com)
  2. Add monitor for your website URL
  3. Set alerts to email/Discord

### Instance Monitoring
The `cloud_manager.py` script includes basic monitoring. For advanced:
- **Prometheus + Grafana** (self-hosted)
- **Datadog** (paid, 14-day trial)

## Security Considerations

### 1. API Key Protection
- Never commit `cloud_config.ini` to GitHub
- Add to `.gitignore`:
  ```
  config/cloud_config.ini
  logs/
  ssh_keys/
  ```

### 2. Website Security
- Enable HTTPS (automatic on GitHub Pages/Vercel)
- Set up CSP headers (optional for advanced users)

### 3. Instance Security
- Use SSH keys, not passwords
- Configure firewall rules
- Regular security updates

## Troubleshooting

### Common Issues

#### Website Not Loading
1. Check GitHub Pages build status
2. Clear browser cache
3. Verify custom DNS settings

#### Cloud API Errors
1. Verify API credentials
2. Check region availability
3. Ensure IAM permissions are correct

#### Form Not Submitting
1. Verify Formspree form ID
2. Check browser console for errors
3. Test with simple form first

### Getting Help
- Discord: `imxyz#1234`
- Email: `hello@imxyz.xyz`
- GitHub Issues: Report bugs

## Next Steps After Deployment

1. **Test the full flow**: Submit form → receive email → create instance → send credentials
2. **Get first customer**: Offer free trial to friends/colleagues
3. **Refine pricing**: Adjust based on actual costs and competition
4. **Automate**: Gradually add more automation as you grow
5. **Market**: Start posting on Reddit, Discord, forums

## Cost Estimate

| Service | Cost | Notes |
|---------|------|-------|
| Domain | $10-15/year | Namecheap/GoDaddy |
| Hosting | $0 | GitHub Pages/Vercel |
| Cloud Resources | Pay-as-you-go | Only when customers pay |
| Formspree | $0 (free tier) | Up to 50 submissions/month |

**Total startup cost**: $10-15 (domain only)

---

**Ready to launch?** Start with Option 1 (GitHub Pages) and get your site live in under 10 minutes!