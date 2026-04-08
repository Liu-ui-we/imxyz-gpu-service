# I built imxyz.xyz to provide cheap GPU compute from China (50-60% cheaper than AWS)

**TL;DR**: I'm a college student who created a service to resell GPU instances from Chinese cloud providers. You get NVIDIA V100/A100 instances at 50-60% lower cost than AWS/GCP/Azure. Perfect for AI training, research, and development work.

## The Problem
As a student working on ML projects, I couldn't afford AWS GPU instances. A100 instances cost $12.50/hour on AWS – that's $300/day for continuous training!

## The Solution
Chinese cloud providers (Aliyun, Tencent Cloud) have significantly lower prices due to local infrastructure costs and government subsidies. I created `imxyz.xyz` to bridge this gap for international users.

## Price Comparison
| GPU Instance | AWS Price | imxyz.xyz Price | Savings |
|--------------|-----------|-----------------|---------|
| NVIDIA V100 (16GB) | $4.10/hour | $2.50/hour | 39% |
| NVIDIA A100 (40GB) | $12.50/hour | $7.80/hour | 38% |
| 8x vCPU + 32GB RAM | $0.68/hour | $0.42/hour | 38% |

**Monthly savings**: Up to $1,200/month for continuous A100 usage.

## How It Works
1. **Submit request** on [imxyz.xyz](https://imxyz.xyz)
2. **Receive quote** within 24 hours
3. **Make payment** (PayPal/Stripe/crypto)
4. **Get SSH access** to your GPU instance
5. **Use for your project** (AI training, rendering, etc.)
6. **Instance auto-terminates** when your time is up

## Target Users
- **AI/ML students & researchers** with limited budgets
- **Startups** prototyping AI models
- **Indie developers** needing GPU power
- **Anyone** tired of cloud provider lock-in

## Technical Details
- **Instances**: Located in China (Beijing/Hangzhou data centers)
- **Network**: ~150-250ms latency from US/EU (fine for batch processing)
- **Software**: Pre-configured with PyTorch, TensorFlow, CUDA drivers
- **Security**: SSH key access only, no data storage on our side

## Why Trust Us?
- **Transparent pricing**: We show exact cloud costs + our 20% service fee
- **No lock-in**: You get full SSH access, can transfer data out anytime
- **Student project**: I'm building this publicly, sharing progress

## Current Status
- ✅ Website live at [imxyz.xyz](https://imxyz.xyz)
- ✅ Manual instance provisioning (I handle each request personally)
- ✅ First 10 customers onboarded
- 🚧 Building automation for instant provisioning
- 🚧 Adding more GPU types and regions

## Special Offer for Reddit Users
Use code **REDDIT25** for 25% off your first month (covers our service fee).

## Questions?
- **Website**: [imxyz.xyz](https://imxyz.xyz)
- **Discord**: [Join our community](https://discord.gg/your-link)
- **Email**: hello@imxyz.xyz

I'd love your feedback, suggestions, or just to chat about AI/cloud computing!

---

**Disclaimer**: This is a student project. Instances are in China, so expect higher latency (150-250ms) compared to local cloud providers. Not suitable for real-time applications.