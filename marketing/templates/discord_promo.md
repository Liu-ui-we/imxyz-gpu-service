# Discord Promotion Messages

Use these messages in AI/ML/developer Discord servers. Adjust based on server rules (some allow promotions, others don't).

## Short Version (for chat)

**For AI/ML servers**:
```
Need affordable GPU compute for your projects? Check out imxyz.xyz - we provide NVIDIA V100/A100 instances from Chinese cloud providers at 50-60% lower cost than AWS/GCP. Perfect for students and researchers on a budget! 🚀

https://imxyz.xyz
```

**For developer servers**:
```
💰 GPU compute doesn't have to break the bank! imxyz.xyz offers cloud GPU instances at half the price of major providers. Great for ML training, rendering, or any compute-intensive work. 

Check our pricing: https://imxyz.xyz/#pricing
```

## Medium Version (for dedicated promo channels)

```
**🚀 Affordable GPU Compute for AI/ML Projects**

Struggling with cloud GPU costs? I built **imxyz.xyz** to solve this exact problem.

**What we offer:**
• NVIDIA V100 instances: $2.50/hour (AWS: $4.10)
• NVIDIA A100 instances: $7.80/hour (AWS: $12.50)  
• CPU instances: $0.42/hour (AWS: $0.68)

**How it works:**
1. Submit request at https://imxyz.xyz
2. We provision GPU instance in China cloud
3. You get SSH access with pre-installed ML frameworks
4. Pay only for what you use (hourly billing)

**Perfect for:**
• Students/researchers with limited budgets
• Startups prototyping AI models  
• Indie developers needing GPU power
• Anyone tired of cloud provider lock-in

**Special offer for Discord users:** Mention "DISCORD20" for 20% off your first month.

Website: https://imxyz.xyz
Discord: [Join our server](https://discord.gg/your-link)
```

## Technical Details (for curious users)

When someone asks how it works technically:

```
**Technical details:**
• **Providers**: Aliyun (Alibaba Cloud), Tencent Cloud
• **Regions**: Beijing, Hangzhou, Shanghai data centers
• **Network**: ~150-250ms latency from US/EU (fine for batch processing)
• **Software**: Pre-configured with PyTorch 2.0+, TensorFlow 2.13+, CUDA 11.8
• **Access**: SSH keys only (no password auth)
• **Data**: We don't store any customer data - you get full control

**Pricing breakdown:**
1. Cloud provider cost (e.g., Aliyun charges $3.50/hour for V100)
2. Our 20% service fee ($0.70/hour)
3. Your total: $4.20/hour (still 38% cheaper than AWS at $4.10/hour)

Yes, we're actually cheaper than AWS for the same hardware!
```

## Response to Common Questions

**Q: Is there a free trial?**
```
We offer a 4-hour free trial for students/researchers. Email hello@imxyz.xyz with your university email and project description.
```

**Q: How do I know my data is safe?**
```
• You get full SSH root access
• We never see your data
• Instances are destroyed after your rental period
• You can encrypt your data before uploading
```

**Q: What about latency?**
```
Instances are in China, so expect 150-250ms latency from US/EU. This is acceptable for:
• AI model training (batch processing)
• Rendering jobs
• Development/testing
• Research computations

Not suitable for real-time applications or gaming.
```

**Q: Can I choose the OS/software?**
```
We offer:
• CentOS 7.9 (default, best GPU driver compatibility)
• Ubuntu 20.04 LTS
• Windows Server 2019 (extra cost)

Pre-installed: PyTorch, TensorFlow, Jupyter, Docker, CUDA toolkit
You can install any additional software via apt/yum.
```

## Server Rules Compliance

**Before posting, check:**
1. Does the server have a #promotions channel?
2. Are self-promotions allowed?
3. Do I need to ask moderators first?
4. Is there a specific format required?

**Best practice:**
1. Join the server and participate for a few days first
2. Check the rules channel
3. Ask in general chat if self-promotion is okay
4. Post in the appropriate channel
5. Don't spam - one message per server is enough

## Tracking Results

Create a spreadsheet to track where you post and the results:

| Server | Date Posted | Responses | Conversions | Notes |
|--------|-------------|-----------|-------------|-------|
| ML Enthusiasts | 2026-04-08 | 12 | 1 | Good engagement |
| PyTorch Community | 2026-04-08 | 8 | 0 | Technical questions |
| AI Researchers | 2026-04-09 | 15 | 2 | High quality leads |

## Follow-up Template

After someone shows interest:

```
Thanks for your interest in imxyz.xyz! 

To get started:
1. Visit https://imxyz.xyz/#order
2. Fill out the request form with your requirements
3. We'll email you a quote within 24 hours
4. You can ask any questions here too!

We're also happy to discuss your specific use case and recommend the best instance type for your needs.
```

---

**Remember**: Provide value first, promote second. Answer questions genuinely, and only promote when it's actually helpful to the conversation.