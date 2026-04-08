#!/usr/bin/env python3
"""
Formspree自动化配置脚本
帮助用户注册Formspree并获取表单ID
"""

import webbrowser
import time
import os
import json
from datetime import datetime

def print_step(step_num, title):
    """打印步骤标题"""
    print(f"\n{'='*60}")
    print(f"步骤 {step_num}: {title}")
    print('='*60)

def main():
    print("🚀 Formspree 自动化配置助手")
    print("此脚本将指导你完成Formspree注册和表单创建")

    # 步骤1：打开Formspree注册页面
    print_step(1, "打开Formspree注册页面")
    print("正在打开浏览器...")
    webbrowser.open("https://formspree.io/register")

    input("请完成注册（使用GitHub/Google/邮箱），完成后按Enter继续...")

    # 步骤2：创建表单
    print_step(2, "创建新表单")
    print("正在打开表单创建页面...")
    webbrowser.open("https://formspree.io/forms")

    print("\n📋 表单配置建议：")
    print("1. 表单名称: 'GPU Instance Request'")
    print("2. 接收邮箱: 你的常用邮箱")
    print("3. 表单字段:")
    print("   - Full Name (必填)")
    print("   - Email Address (必填)")
    print("   - GPU Type (下拉选择)")
    print("   - Duration (下拉选择)")
    print("   - Additional Requirements (文本框)")
    print("   - Budget (文本)")

    input("创建表单后，按Enter继续获取表单ID...")

    # 步骤3：获取表单ID
    print_step(3, "获取表单ID")
    print("\n🔍 如何找到你的Formspree表单ID：")
    print("1. 在Formspree仪表板，点击你的表单")
    print("2. 查看表单设置 → 'Integration' 或 'Code' 标签")
    print("3. 找到表单URL，类似：https://formspree.io/f/xqknvqgw")
    print("4. 表单ID就是 'xqknvqgw' (f/后面的部分)")
    print("\n或者查看表单的HTML代码：")
    print('<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">')

    form_id = input("\n请输入你的Formspree表单ID: ").strip()

    # 验证表单ID格式
    if not form_id or len(form_id) < 3:
        print("⚠️  表单ID格式不正确，使用默认示例")
        form_id = "your-form-id"

    # 步骤4：更新网站代码
    print_step(4, "更新网站代码")

    # 要更新的文件列表
    files_to_update = [
        "/c/Users/31883/Documents/imxyz-gpu-service/index.html",
        "/c/Users/31883/Documents/imxyz-gpu-service/public/index.html"
    ]

    for file_path in files_to_update:
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换表单ID
                old_action = 'action="https://formspree.io/f/your-form-id"'
                new_action = f'action="https://formspree.io/f/{form_id}"'

                if old_action in content:
                    content = content.replace(old_action, new_action)

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

                    print(f"✅ 已更新: {file_path}")
                    print(f"   旧: {old_action}")
                    print(f"   新: {new_action}")
                else:
                    # 尝试其他可能的格式
                    old_action_alt = 'action="https://formspree.io/f/xqknvqgw"'
                    if old_action_alt in content:
                        content = content.replace(old_action_alt, new_action)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        print(f"✅ 已更新: {file_path} (替代格式)")
                    else:
                        print(f"⚠️  未找到表单action标签: {file_path}")

            except Exception as e:
                print(f"❌ 更新失败 {file_path}: {e}")
        else:
            print(f"📄 文件不存在: {file_path}")

    # 步骤5：创建配置记录
    print_step(5, "创建配置记录")

    config = {
        "formspree": {
            "form_id": form_id,
            "form_url": f"https://formspree.io/f/{form_id}",
            "dashboard_url": "https://formspree.io/forms",
            "configured_at": datetime.now().isoformat(),
            "notes": "Formspree表单配置"
        },
        "website": {
            "url": "https://imxyz.xyz",
            "github_pages": "https://liu-ui-we.github.io/imxyz-gpu-service",
            "form_location": "index.html 第180行"
        }
    }

    config_file = "/c/Users/31883/Documents/imxyz-gpu-service/config/formspree_config.json"
    os.makedirs(os.path.dirname(config_file), exist_ok=True)

    with open(config_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print(f"✅ 配置已保存: {config_file}")

    # 步骤6：测试表单
    print_step(6, "测试表单")
    print("\n🔧 现在测试你的表单：")
    print("1. 打开网站: https://liu-ui-we.github.io/imxyz-gpu-service/")
    print("2. 滚动到 'Order Your GPU Instance' 部分")
    print("3. 填写测试信息并提交")
    print("4. 检查你的邮箱是否收到Formspree通知")

    print("\n📧 测试数据建议：")
    print("   Name: Test User")
    print("   Email: 你的邮箱")
    print("   GPU Type: V100")
    print("   Duration: 1 Day")
    print("   Requirements: Test submission")

    print("\n🎉 配置完成！")
    print(f"你的Formspree表单ID: {form_id}")
    print(f"表单URL: https://formspree.io/f/{form_id}")

if __name__ == "__main__":
    main()