# Email Templates for imxyz.xyz

Use these templates for customer communication. Personalize where appropriate.

## 1. Initial Quote Email

**Subject**: Quote for your GPU instance request at imxyz.xyz

**Body**:
```
Hi [Customer Name],

Thanks for your interest in imxyz.xyz GPU compute service! Here's your customized quote based on your requirements:

**Order Details:**
- GPU Type: [V100/A100/RTX 3090]
- Instance Type: [e.g., 8x vCPU, 32GB RAM]
- Duration: [X hours/days/weeks]
- Region: [China East 1 / China North 2]
- Software: [PyTorch/TensorFlow/Jupyter/etc.]

**Cost Breakdown:**
- Cloud provider cost: $[X.XX]/hour
- Our service fee (20%): $[X.XX]/hour
- **Total rate: $[X.XX]/hour**
- Estimated total ([Y] hours): **$[XXX.XX]**

**Payment Options:**
1. **PayPal**: [PayPal payment link]
2. **Stripe**: [Stripe payment link]
3. **Cryptocurrency** (BTC/ETH/USDT): [Wallet address]

**Next Steps:**
1. Choose payment method above
2. We'll provision your instance (typically within 2-4 hours after payment)
3. You'll receive SSH credentials via email
4. Start using your GPU instance!

**Questions?**
- Reply to this email
- Join our Discord: [Discord invite link]
- Visit: https://imxyz.xyz

Looking forward to helping with your project!

Best regards,
[Your Name]
imxyz.xyz Team
```

## 2. Payment Confirmation & Instance Details

**Subject**: Your imxyz.xyz GPU instance is ready! SSH credentials enclosed

**Body**:
```
Hi [Customer Name],

Great news! Your GPU instance has been provisioned and is ready for use.

**Instance Information:**
- Instance ID: [e.g., i-xxxxxxxx]
- Public IP: [XXX.XXX.XXX.XXX]
- SSH Port: 22
- SSH Username: [root/ubuntu/ecs-user]
- Access Method: SSH key authentication (see attached key or use password below)
- Region: [China East 1]
- GPU: [NVIDIA V100 16GB]
- Available until: [Date and time]

**SSH Access:**
```
ssh -i [attached_key.pem] [username]@[public_ip]
```
Or use password (less secure): [temporary password - change immediately]

**Pre-installed Software:**
- PyTorch 2.0.0 with CUDA 11.8
- TensorFlow 2.13.0
- Jupyter Notebook (port 8888)
- Docker & NVIDIA Docker
- CUDA Toolkit 11.8
- cuDNN 8.9

**Getting Started:**
1. Connect via SSH (see above)
2. Check GPU status: `nvidia-smi`
3. Start Jupyter: `jupyter notebook --ip=0.0.0.0 --port=8888`
4. Access Jupyter at: `http://[public_ip]:8888`

**Important Notes:**
- **Latency**: Expect 150-250ms from US/EU due to China location
- **Data Security**: We don't access your data. You have full control.
- **Backups**: We don't backup your data. Please backup important files.
- **Support**: Basic support via email/Discord. Response time: <24 hours.

**Billing:**
- Instance will auto-terminate at [date/time]
- You'll receive a usage report after termination
- If you need more time, email us before expiration

**Need Help?**
- Discord: [Discord invite]
- Email: hello@imxyz.xyz
- Docs: https://imxyz.xyz/#how-it-works

Happy computing! 🚀

Best regards,
[Your Name]
imxyz.xyz Team
```

## 3. Instance Termination Notice

**Subject**: Your imxyz.xyz GPU instance has been terminated

**Body**:
```
Hi [Customer Name],

Your GPU instance ([Instance ID]) has been terminated as scheduled at [termination time].

**Usage Summary:**
- Total runtime: [X] hours [Y] minutes
- Total cost: $[XXX.XX]
- Data destroyed: All instance data has been permanently deleted

**Next Steps:**
1. **Download your data**: If you haven't already, ensure you've downloaded all important files from the instance.
2. **Feedback**: We'd love to hear about your experience: [Feedback form link]
3. **Future needs**: Need GPU compute again? Just submit a new request at https://imxyz.xyz

**Invoice**: A detailed invoice is attached to this email.

**Thank you** for using imxyz.xyz! We hope the GPU compute helped with your project.

Best regards,
[Your Name]
imxyz.xyz Team
```

## 4. Follow-up After Trial/First Use

**Subject**: How was your imxyz.xyz GPU experience?

**Body**:
```
Hi [Customer Name],

Hope your GPU instance helped with your [project type - e.g., AI model training]!

We're always looking to improve our service and would appreciate your feedback:

1. **Overall experience**: How was the setup process?
2. **Performance**: Did the GPU meet your compute needs?
3. **Support**: Was our assistance helpful?
4. **Suggestions**: What could we do better?

**Quick feedback link**: [Google Form/SurveyMonkey link]

**Special Offer**: As a returning customer, you get 15% off your next rental. Use code RETURN15 when submitting your next request.

Thanks for being an early user of imxyz.xyz!

Best regards,
[Your Name]
imxyz.xyz Team
```

## 5. Outreach to AI/ML Communities

**Subject**: Affordable GPU compute for your AI projects

**Body**:
```
Hi [Community Name],

I'm [Your Name], a [your background - e.g., computer science student] building imxyz.xyz - a service that provides GPU compute instances from Chinese cloud providers at 50-60% lower cost than AWS/GCP/Azure.

**Why this matters:**
- Students/researchers can afford more compute time
- Startups can prototype without huge cloud bills
- Everyone gets an alternative to cloud provider lock-in

**Example savings:**
- NVIDIA A100: $7.80/hour (vs $12.50/hour on AWS)
- Monthly A100 usage: ~$5,700 (vs ~$9,000 on AWS)

**For your community:**
- **Free trial**: 4-hour free GPU instance for students
- **Discount**: 25% off first month for community members
- **Support**: We offer basic technical support for setup

**Could we:**
1. Share this with your community if relevant?
2. Offer a community-exclusive discount?
3. Answer any questions you have?

Website: https://imxyz.xyz
Example pricing: https://imxyz.xyz/#pricing

Thanks for your time!

Best regards,
[Your Name]
imxyz.xyz Team
```

## 6. Customer Support Template

**Subject**: Re: Your question about [topic]

**Body**:
```
Hi [Customer Name],

Thanks for reaching out about [their question topic]. Here's some information that might help:

[Answer to their specific question]

**Common Solutions:**
1. **SSH connection issues**: Ensure you're using the correct key and username
2. **GPU not detected**: Run `nvidia-smi` to check driver status
3. **Software missing**: Use `pip install` or `apt-get install` as needed
4. **Performance issues**: Check resource usage with `htop` or `nvidia-smi`

**If you need further help:**
1. **Error messages**: Please share the exact error message
2. **Commands tried**: What commands have you run?
3. **Expected vs actual**: What were you trying to do vs what happened?

**Support Channels:**
- **Email**: Reply to this thread
- **Discord**: [Invite link] for faster responses
- **Documentation**: https://imxyz.xyz/#how-it-works

We'll do our best to resolve your issue promptly!

Best regards,
[Your Name]
imxyz.xyz Team
```

## 7. Invoice Template (Plain Text)

**Subject**: Invoice #[Invoice Number] from imxyz.xyz

**Body**:
```
INVOICE
imxyz.xyz
[Your Address]
[Your Email]
[Your Website]

BILL TO:
[Customer Name]
[Customer Email]

INVOICE #: [Number]
DATE: [Date]
DUE DATE: [Date]

DESCRIPTION:
GPU Compute Service - [GPU Type] Instance
Instance ID: [Instance ID]
Period: [Start Date] to [End Date]
Total hours: [X] hours

COST BREAKDOWN:
- Base compute cost: $[X.XX]/hour × [Y] hours = $[XXX.XX]
- Service fee (20%): $[X.XX]/hour × [Y] hours = $[XXX.XX]
- **TOTAL: $[XXX.XX]**

Payment method: [PayPal/Stripe/Crypto]
Payment date: [Date]
Transaction ID: [Transaction ID]

Thank you for your business!

Questions? Contact hello@imxyz.xyz
```

## Email Best Practices

### 1. Timing
- **Initial quote**: Send within 24 hours of request
- **Credentials**: Send within 2-4 hours after payment
- **Termination notice**: Send immediately after instance termination
- **Follow-up**: Send 1-2 days after service ends

### 2. Personalization
- Use customer name
- Reference their specific use case
- Mention any custom configuration

### 3. Clarity
- Bullet points for key information
- Clear calls to action
- Contact information prominently displayed

### 4. Professionalism
- Check spelling and grammar
- Use consistent formatting
- Include disclaimer if needed

### 5. Automation Tips
- Use email templates in Gmail/Outlook
- Consider tools like Mailchimp for newsletters
- Set up auto-responders for common questions

---

**Note**: Always test email templates before sending to customers. Ensure links work and formatting looks good on both desktop and mobile.