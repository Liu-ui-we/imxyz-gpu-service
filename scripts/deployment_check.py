#!/usr/bin/env python3
"""
imxyz.xyz 部署完成度检查脚本
检查网站、DNS、表单等各项配置状态
"""

import requests
import json
import os
import sys
import time
from datetime import datetime

def check_github_pages():
    """检查GitHub Pages状态"""
    print("\n🔍 检查GitHub Pages...")

    urls = [
        "https://liu-ui-we.github.io/imxyz-gpu-service/",
        "http://imxyz.xyz/",
        "https://imxyz.xyz/"
    ]

    results = {}

    for url in urls:
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10, allow_redirects=True)
            elapsed = time.time() - start_time

            results[url] = {
                "status_code": response.status_code,
                "response_time": f"{elapsed:.2f}s",
                "final_url": response.url,
                "content_length": len(response.content),
                "success": response.status_code == 200
            }

            status = "✅" if response.status_code == 200 else "⚠️"
            print(f"  {status} {url}")
            print(f"    状态: {response.status_code} | 时间: {elapsed:.2f}s")

        except requests.RequestException as e:
            results[url] = {
                "error": str(e),
                "success": False
            }
            print(f"  ❌ {url}")
            print(f"    错误: {e}")

    return results

def check_formspree_config():
    """检查Formspree配置"""
    print("\n🔍 检查Formspree配置...")

    config_file = "/c/Users/31883/Documents/imxyz-gpu-service/config/formspree_config.json"

    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)

            form_id = config.get("formspree", {}).get("form_id", "未配置")

            if form_id and form_id != "your-form-id":
                print(f"  ✅ Formspree已配置")
                print(f"    表单ID: {form_id}")
                print(f"    表单URL: https://formspree.io/f/{form_id}")

                # 测试表单链接
                test_url = f"https://formspree.io/f/{form_id}"
                try:
                    response = requests.get(test_url, timeout=5)
                    if response.status_code == 200:
                        print(f"    表单链接: 有效")
                except:
                    print(f"    表单链接: 需要验证")

                return {
                    "configured": True,
                    "form_id": form_id,
                    "form_url": f"https://formspree.io/f/{form_id}"
                }
            else:
                print(f"  ⚠️  Formspree未配置")
                print(f"    请运行: python scripts/formspree_setup.py")
                return {"configured": False}

        except json.JSONDecodeError:
            print(f"  ❌ 配置文件格式错误")
            return {"configured": False}
    else:
        print(f"  📝 Formspree未配置")
        print(f"    请运行: python scripts/formspree_setup.py")
        return {"configured": False}

def check_dns_config():
    """检查DNS配置"""
    print("\n🔍 检查DNS配置...")

    config_file = "/c/Users/31883/Documents/imxyz-gpu-service/config/dns_config.json"

    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)

            registrar = config.get("registrar", "未知")
            configured_at = config.get("configured_at", "未知")

            print(f"  ✅ DNS配置已记录")
            print(f"    注册商: {registrar}")
            print(f"    配置时间: {configured_at}")

            return {
                "configured": True,
                "registrar": registrar,
                "configured_at": configured_at
            }

        except json.JSONDecodeError:
            print(f"  ❌ DNS配置文件格式错误")
            return {"configured": False}
    else:
        print(f"  📝 DNS未配置")
        print(f"    请运行: python scripts/dns_config_helper.py")
        return {"configured": False}

def check_cloud_config():
    """检查云服务配置"""
    print("\n🔍 检查云服务配置...")

    config_file = "/c/Users/31883/Documents/imxyz-gpu-service/config/cloud_config.ini"
    example_file = "/c/Users/31883/Documents/imxyz-gpu-service/config/cloud_config.ini.example"

    if os.path.exists(config_file):
        try:
            import configparser
            config = configparser.ConfigParser()
            config.read(config_file)

            # 检查是否已配置凭证
            aliyun_key = config.get("aliyun", "access_key_id", fallback="")
            if aliyun_key and aliyun_key != "YOUR_ALIYUN_ACCESS_KEY_ID":
                print(f"  ✅ 云服务配置已设置")
                print(f"    提供商: 阿里云")
                return {"configured": True}
            else:
                print(f"  ⚠️  云服务凭证未配置")
                print(f"    请编辑: {config_file}")
                return {"configured": False}

        except Exception as e:
            print(f"  ❌ 配置文件读取错误: {e}")
            return {"configured": False}
    else:
        print(f"  📝 云服务配置未初始化")
        print(f"    请复制: cp {example_file} {config_file}")
        return {"configured": False}

def check_project_structure():
    """检查项目结构"""
    print("\n🔍 检查项目结构...")

    required_dirs = [
        "/c/Users/31883/Documents/imxyz-gpu-service",
        "/c/Users/31883/Documents/imxyz-gpu-service/config",
        "/c/Users/31883/Documents/imxyz-gpu-service/scripts",
        "/c/Users/31883/Documents/imxyz-gpu-service/marketing",
        "/c/Users/31883/Documents/imxyz-gpu-service/docs"
    ]

    required_files = [
        "/c/Users/31883/Documents/imxyz-gpu-service/index.html",
        "/c/Users/31883/Documents/imxyz-gpu-service/css/style.css",
        "/c/Users/31883/Documents/imxyz-gpu-service/js/script.js",
        "/c/Users/31883/Documents/imxyz-gpu-service/scripts/cloud_manager.py",
        "/c/Users/31883/Documents/imxyz-gpu-service/config/cloud_config.ini.example",
        "/c/Users/31883/Documents/imxyz-gpu-service/README.md"
    ]

    all_good = True

    for dir_path in required_dirs:
        if os.path.exists(dir_path):
            print(f"  ✅ 目录存在: {os.path.basename(dir_path)}")
        else:
            print(f"  ❌ 目录缺失: {os.path.basename(dir_path)}")
            all_good = False

    for file_path in required_files:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            print(f"  ✅ 文件存在: {os.path.basename(file_path)} ({file_size} bytes)")
        else:
            print(f"  ❌ 文件缺失: {os.path.basename(file_path)}")
            all_good = False

    return {"complete": all_good}

def generate_report(results):
    """生成部署报告"""
    print("\n" + "="*70)
    print("📊 imxyz.xyz 部署完成度报告")
    print("="*70)

    report = {
        "timestamp": datetime.now().isoformat(),
        "project": "imxyz.xyz GPU Compute Service",
        "status": {}
    }

    # 计算完成度
    total_checks = 0
    passed_checks = 0

    for check_name, check_result in results.items():
        if isinstance(check_result, dict):
            if check_result.get("success") or check_result.get("configured") or check_result.get("complete"):
                passed_checks += 1
                status = "✅ 通过"
            else:
                status = "❌ 未完成"
            total_checks += 1
        elif isinstance(check_result, list):
            # 处理多个URL的结果
            url_results = check_result
            success_count = sum(1 for r in url_results.values() if r.get("success"))
            status = f"✅ {success_count}/{len(url_results)} 通过"
            total_checks += 1
            if success_count == len(url_results):
                passed_checks += 1

    completion_rate = (passed_checks / total_checks * 100) if total_checks > 0 else 0

    print(f"\n📈 总体完成度: {completion_rate:.1f}% ({passed_checks}/{total_checks})")

    if completion_rate >= 80:
        print("🎉 恭喜！项目已接近完成，可以开始运营！")
    elif completion_rate >= 50:
        print("👍 进展良好，继续完成剩余配置")
    else:
        print("🚧 需要完成更多基础配置")

    print("\n📋 下一步行动:")

    if completion_rate < 100:
        if not results.get("formspree", {}).get("configured"):
            print("  1. 📝 配置Formspree表单: python scripts/formspree_setup.py")

        if not results.get("dns", {}).get("configured"):
            print("  2. 🌐 配置DNS: python scripts/dns_config_helper.py")

        if not results.get("cloud", {}).get("configured"):
            print("  3. ☁️  配置云服务: 编辑 config/cloud_config.ini")

    print("\n  4. 🚀 开始营销:")
    print("     • 使用 marketing/templates/reddit_intro.md 发布到Reddit")
    print("     • 加入AI/ML Discord群组推广")
    print("     • 联系潜在客户提供免费试用")

    print("\n  5. 💰 获取第一批客户:")
    print("     • 提供1-2个免费试用名额")
    print("     • 收集反馈优化流程")
    print("     • 建立口碑推荐")

    # 保存报告
    report_file = "/c/Users/31883/Documents/imxyz-gpu-service/config/deployment_report.json"
    os.makedirs(os.path.dirname(report_file), exist_ok=True)

    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n📄 详细报告已保存: {report_file}")

    return completion_rate

def main():
    """主函数"""
    print("🚀 imxyz.xyz 部署状态检查")
    print("="*60)

    results = {}

    # 执行各项检查
    results["github_pages"] = check_github_pages()
    results["project_structure"] = check_project_structure()
    results["formspree"] = check_formspree_config()
    results["dns"] = check_dns_config()
    results["cloud"] = check_cloud_config()

    # 生成报告
    completion_rate = generate_report(results)

    print("\n" + "="*60)
    print("💡 提示:")
    print("• 网站已上线: https://liu-ui-we.github.io/imxyz-gpu-service/")
    print("• 域名配置后: https://imxyz.xyz/")
    print("• 自动化脚本: scripts/cloud_manager.py")
    print("• 营销材料: marketing/templates/")
    print("• 详细文档: docs/")
    print("="*60)

    return completion_rate

if __name__ == "__main__":
    try:
        completion = main()
        sys.exit(0 if completion >= 80 else 1)
    except KeyboardInterrupt:
        print("\n\n操作已取消")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 检查过程中出错: {e}")
        sys.exit(1)