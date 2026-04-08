#!/usr/bin/env python3
"""
imxyz.xyz 快速启动脚本
一站式配置和启动你的GPU算力出海业务
"""

import os
import sys
import subprocess
import webbrowser
import time
from datetime import datetime

class QuickStart:
    """快速启动类"""

    def __init__(self):
        self.project_root = "/c/Users/31883/Documents/imxyz-gpu-service"
        self.checkmarks = {
            "✅": "完成",
            "🔄": "进行中",
            "❌": "失败",
            "⚠️": "警告",
            "📝": "待配置"
        }

    def print_header(self):
        """打印标题"""
        print("\n" + "="*70)
        print("🚀 imxyz.xyz GPU算力出海业务 - 快速启动")
        print("="*70)
        print("作者: Liu-ui-we (大四学生)")
        print("启动时间: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("\n🎯 目标: 在30分钟内启动你的业务，获得第一个客户")
        print("="*70)

    def run_command(self, cmd, description):
        """运行命令并显示状态"""
        print(f"\n{description}...")
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"  ✅ 完成")
                if result.stdout.strip():
                    print(f"    输出: {result.stdout.strip()}")
                return True
            else:
                print(f"  ❌ 失败")
                if result.stderr:
                    print(f"    错误: {result.stderr.strip()}")
                return False
        except Exception as e:
            print(f"  ❌ 异常: {e}")
            return False

    def step_1_check_prerequisites(self):
        """步骤1: 检查前置条件"""
        print("\n1️⃣ 检查前置条件")

        checks = []

        # 检查Python
        python_check = self.run_command("python --version", "检查Python版本")
        checks.append(("Python 3.8+", python_check))

        # 检查Git
        git_check = self.run_command("git --version", "检查Git")
        checks.append(("Git", git_check))

        # 检查pip
        pip_check = self.run_command("pip --version", "检查pip")
        checks.append(("pip", pip_check))

        # 检查项目目录
        if os.path.exists(self.project_root):
            print("  ✅ 项目目录存在")
            checks.append(("项目目录", True))
        else:
            print("  ❌ 项目目录不存在")
            checks.append(("项目目录", False))

        # 打印总结
        print("\n📊 前置条件检查总结:")
        for check_name, check_result in checks:
            status = "✅" if check_result else "❌"
            print(f"  {status} {check_name}")

        all_passed = all(result for _, result in checks)
        return all_passed

    def step_2_configure_formspree(self):
        """步骤2: 配置Formspree"""
        print("\n2️⃣ 配置Formspree表单")

        print("📋 配置步骤:")
        print("  1. 访问 https://formspree.io")
        print("  2. 用GitHub/Google/邮箱注册")
        print("  3. 创建新表单: 'GPU Instance Request'")
        print("  4. 获取表单ID (如 'xqknvqgw')")

        webbrowser.open("https://formspree.io/register")

        print("\n📝 请完成Formspree注册，然后:")
        input("  按Enter键继续（完成后）...")

        # 运行Formspree配置脚本
        formspree_script = os.path.join(self.project_root, "scripts", "formspree_setup.py")
        if os.path.exists(formspree_script):
            return self.run_command(f"python {formspree_script}", "配置Formspree表单")
        else:
            print("  ⚠️  Formspree配置脚本不存在")
            return False

    def step_3_configure_dns(self):
        """步骤3: 配置DNS"""
        print("\n3️⃣ 配置DNS记录")

        print("📋 你需要将 imxyz.xyz 指向:")
        print("  liu-ui-we.github.io 或对应的IP地址")

        # 运行DNS配置助手
        dns_script = os.path.join(self.project_root, "scripts", "dns_config_helper.py")
        if os.path.exists(dns_script):
            return self.run_command(f"python {dns_script}", "配置DNS记录")
        else:
            print("  ⚠️  DNS配置脚本不存在")
            return False

    def step_4_test_website(self):
        """步骤4: 测试网站"""
        print("\n4️⃣ 测试网站")

        test_urls = [
            ("临时地址", "https://liu-ui-we.github.io/imxyz-gpu-service/"),
            ("自定义域名", "https://imxyz.xyz/")
        ]

        results = []

        for name, url in test_urls:
            print(f"\n🔍 测试 {name}:")
            print(f"  URL: {url}")

            try:
                # 使用curl测试
                cmd = f"curl -s -o /dev/null -w \"%{{http_code}}\" {url}"
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

                if result.returncode == 0:
                    status_code = result.stdout.strip()
                    if status_code == "200":
                        print(f"  ✅ 可达 (状态码: {status_code})")
                        results.append((name, True))
                    else:
                        print(f"  ⚠️  返回状态码: {status_code}")
                        results.append((name, False))
                else:
                    print(f"  ❌ 测试失败")
                    results.append((name, False))

            except Exception as e:
                print(f"  ❌ 异常: {e}")
                results.append((name, False))

        # 提供访问链接
        print("\n🌐 网站访问地址:")
        for name, url in test_urls:
            print(f"  • {name}: {url}")

        return all(result for _, result in results)

    def step_5_configure_cloud_provider(self):
        """步骤5: 配置云服务提供商"""
        print("\n5️⃣ 配置云服务提供商")

        print("📋 你需要配置以下至少一项:")

        providers = [
            ("阿里云 (Alibaba Cloud)",
             "https://ram.console.aliyun.com/users",
             "获取AccessKey ID和Secret"),
            ("腾讯云 (Tencent Cloud)",
             "https://console.cloud.tencent.com/cam/capi",
             "获取SecretId和SecretKey")
        ]

        webbrowser.open("https://ram.console.aliyun.com/users")

        print("\n📝 操作步骤:")
        print("  1. 选择云服务提供商")
        print("  2. 注册/登录获取API密钥")
        print("  3. 将密钥填入 config/cloud_config.ini")
        print("  4. 测试连接")

        print("\n🔧 快速配置:")
        print("  复制配置文件:")
        print("  cp config/cloud_config.ini.example config/cloud_config.ini")

        print("\n  编辑配置文件:")
        print("  nano config/cloud_config.ini")

        # 检查配置文件是否存在
        config_file = os.path.join(self.project_root, "config", "cloud_config.ini")
        if os.path.exists(config_file):
            print(f"\n  ✅ 配置文件已存在: {config_file}")
            return True
        else:
            print(f"\n  📝 配置文件不存在，请创建")
            return False

    def step_6_get_first_customer(self):
        """步骤6: 获取第一个客户"""
        print("\n6️⃣ 获取第一个客户")

        print("🎯 目标: 在24小时内获得第一个付费客户")

        print("\n📋 行动计划:")

        actions = [
            ("📱 社交媒体", [
                "1. 在Reddit r/MachineLearning发布",
                "2. 加入AI/ML Discord群组",
                "3. 在相关论坛分享"
            ]),
            ("🎯 精准营销", [
                "1. 联系同学/朋友 (免费试用)",
                "2. 寻找AI项目学生",
                "3. 联系小型研究团队"
            ]),
            ("💰 首次优惠", [
                "1. 提供50%折扣首单",
                "2. 免费4小时试用",
                "3. 推荐奖励计划"
            ])
        ]

        for category, steps in actions:
            print(f"\n  {category}:")
            for step in steps:
                print(f"    {step}")

        print("\n🔧 营销工具:")
        print("  • Reddit帖子: marketing/templates/reddit_intro.md")
        print("  • Discord文案: marketing/templates/discord_promo.md")
        print("  • 邮件模板: marketing/templates/email_templates.md")

        print("\n📊 预期成果:")
        print("  • 第1周: 1-3个付费客户")
        print("  • 第2周: 3-5个付费客户")
        print("  • 第1月: 10+个付费客户")

        return True  # 这一步总是返回True，需要用户手动执行

    def step_7_start_marketing(self):
        """步骤7: 开始营销"""
        print("\n7️⃣ 启动营销活动")

        print("🚀 立即行动清单:")

        actions = [
            ("1️⃣ 发布Reddit帖子", {
                "平台": "r/MachineLearning, r/deeplearning",
                "模板": "marketing/templates/reddit_intro.md",
                "行动": "复制内容，发布到Reddit"
            }),
            ("2️⃣ 加入Discord群组", {
                "目标": "FastAI, PyTorch, TensorFlow群组",
                "模板": "marketing/templates/discord_promo.md",
                "行动": "加入3个群组，分享服务"
            }),
            ("3️⃣ 联系潜在客户", {
                "目标": "同学、朋友、小型团队",
                "模板": "marketing/templates/email_templates.md",
                "行动": "发送5个个性化邀请"
            }),
            ("4️⃣ 测试完整流程", {
                "目标": "从订单到交付",
                "步骤": "模拟客户下单→创建实例→交付",
                "行动": "完成一次端到端测试"
            })
        ]

        for title, details in actions:
            print(f"\n{title}")
            for key, value in details.items():
                print(f"  {key}: {value}")

        print("\n⏰ 时间安排:")
        print("  • 今天: 完成前3项行动")
        print("  • 明天: 联系10个潜在客户")
        print("  • 本周: 获得第一个付费客户")

        return True

    def step_8_generate_launch_report(self):
        """步骤8: 生成启动报告"""
        print("\n8️⃣ 生成启动报告")

        report = {
            "project": "imxyz.xyz GPU Compute Service",
            "launch_date": datetime.now().isoformat(),
            "status": "快速启动完成",
            "next_steps": [],
            "resources": {
                "website": "https://imxyz.xyz",
                "github": "https://github.com/Liu-ui-we/imxyz-gpu-service",
                "docs": os.path.join(self.project_root, "docs"),
                "scripts": os.path.join(self.project_root, "scripts"),
                "marketing": os.path.join(self.project_root, "marketing", "templates")
            },
            "estimated_timeline": {
                "day_1": "完成基本配置，开始营销",
                "day_3": "获得第一批咨询",
                "week_1": "获得第一个付费客户",
                "month_1": "稳定月收入 $500+"
            }
        }

        # 保存报告
        report_file = os.path.join(self.project_root, "config", "launch_report.json")
        os.makedirs(os.path.dirname(report_file), exist_ok=True)

        import json
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"\n📄 启动报告已保存: {report_file}")

        print("\n🎉 恭喜！你的imxyz.xyz GPU算力出海业务已准备就绪！")
        print("\n📈 下一步：")
        print("  1. 按照营销计划行动")
        print("  2. 获取第一个付费客户")
        print("  3. 优化流程和自动化")
        print("  4. 扩展客户群和收入")

        return True

    def run_all_steps(self):
        """运行所有步骤"""
        self.print_header()

        steps = [
            ("检查前置条件", self.step_1_check_prerequisites),
            ("配置Formspree表单", self.step_2_configure_formspree),
            ("配置DNS记录", self.step_3_configure_dns),
            ("测试网站", self.step_4_test_website),
            ("配置云服务", self.step_5_configure_cloud_provider),
            ("获取第一个客户", self.step_6_get_first_customer),
            ("启动营销活动", self.step_7_start_marketing),
            ("生成启动报告", self.step_8_generate_launch_report)
        ]

        results = []

        for step_name, step_func in steps:
            print(f"\n📌 {step_name}")
            print("-" * 50)

            try:
                result = step_func()
                results.append((step_name, result))

                if result:
                    print(f"\n✅ {step_name} - 完成")
                else:
                    print(f"\n⚠️  {step_name} - 遇到问题，请检查")

                if step_name != "生成启动报告":
                    input("\n按Enter键继续下一步...")

            except KeyboardInterrupt:
                print(f"\n⏹️  {step_name} - 用户中断")
                results.append((step_name, False))
                break
            except Exception as e:
                print(f"\n❌ {step_name} - 错误: {e}")
                results.append((step_name, False))

        # 打印总结
        print("\n" + "="*70)
        print("📊 快速启动总结")
        print("="*70)

        completed = sum(1 for _, result in results if result)
        total = len(results)

        print(f"\n✅ 完成步骤: {completed}/{total}")

        for step_name, result in results:
            status = "✅" if result else "❌"
            print(f"  {status} {step_name}")

        completion_rate = (completed / total * 100) if total > 0 else 0
        print(f"\n📈 总体完成率: {completion_rate:.1f}%")

        if completion_rate >= 80:
            print("\n🎉 启动成功！你的业务已准备好迎接客户！")
        elif completion_rate >= 50:
            print("\n👍 启动进行中，请完成剩余配置")
        else:
            print("\n🔄 启动需要更多配置，请参考文档")

        return completion_rate

def main():
    """主函数"""
    print("🚀 imxyz.xyz GPU算力出海业务 - 快速启动向导")
    print("⏰ 预计时间: 30分钟")
    print("🎯 目标: 完成基本配置，开始获取客户")

    # 确认启动
    print("\n📋 将要执行的步骤:")
    steps = [
        "1. 检查系统环境 (Python, Git)",
        "2. 配置订单表单 (Formspree)",
        "3. 设置域名DNS (imxyz.xyz)",
        "4. 测试网站访问",
        "5. 配置云服务API",
        "6. 制定获客计划",
        "7. 启动营销活动",
        "8. 生成启动报告"
    ]

    for step in steps:
        print(f"  {step}")

    response = input("\n是否继续？ (y/N): ").strip().lower()

    if response not in ['y', 'yes']:
        print("\n启动已取消")
        sys.exit(0)

    # 运行快速启动
    quickstart = QuickStart()

    try:
        completion = quickstart.run_all_steps()

        print("\n" + "="*70)
        print("🎯 立即行动:")
        print("="*70)

        print("\n📱 今日必做:")
        print("  1. 在Reddit发布: r/MachineLearning")
        print("  2. 加入3个AI Discord群组")
        print("  3. 联系5位潜在客户")

        print("\n💰 收入目标:")
        print("  • 本周: $50+")
        print("  • 本月: $500+")
        print("  • 本年: $10,000+")

        print("\n🔗 重要链接:")
        print("  • 网站: https://imxyz.xyz")
        print("  • GitHub: https://github.com/Liu-ui-we/imxyz-gpu-service")
        print("  • 文档: file://" + quickstart.project_root + "/docs")

        print("\n💪 开始你的创业之旅吧！")
        print("遇到问题时，随时回来查看文档或寻求帮助")

        return completion

    except KeyboardInterrupt:
        print("\n\n操作已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 启动过程中出错: {e}")
        sys.exit(1)

if __name__ == "__main__":
    completion_rate = main()
    sys.exit(0 if completion_rate >= 80 else 1)