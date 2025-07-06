#!/usr/bin/env python3
"""
自动设置Cursor MCP SSH工具配置
"""

import json
import os
import shutil
from pathlib import Path

def setup_cursor_mcp():
    """设置Cursor MCP配置"""
    print("🚀 开始设置Cursor MCP SSH工具...")
    
    # Cursor设置文件路径
    cursor_settings_path = Path.home() / "Library/Application Support/Cursor/User/settings.json"
    
    # 检查Cursor设置文件是否存在
    if not cursor_settings_path.exists():
        print(f"❌ Cursor设置文件不存在: {cursor_settings_path}")
        print("请先安装并运行Cursor编辑器")
        return False
    
    # 读取当前设置
    try:
        with open(cursor_settings_path, 'r', encoding='utf-8') as f:
            settings = json.load(f)
    except Exception as e:
        print(f"❌ 读取Cursor设置文件失败: {e}")
        return False
    
    # 检查是否已有MCP配置
    if "mcpServers" in settings:
        print("⚠️  检测到现有MCP配置，将更新SSH工具配置")
    else:
        print("✓ 添加新的MCP配置")
    
    # 获取当前项目路径
    current_dir = Path.cwd()
    ssh_tool_path = current_dir / "mcp_ssh_tool.py"
    
    if not ssh_tool_path.exists():
        print(f"❌ SSH工具文件不存在: {ssh_tool_path}")
        return False
    
    # 添加MCP配置
    mcp_config = {
        "ssh-tool": {
            "command": "python3",
            "args": [str(ssh_tool_path)],
            "env": {
                "SSH_HOST": "8.155.24.17",
                "SSH_USER": "root",
                "SSH_PASSWORD": "D4u1o5!@",
                "SSH_PORT": "22"
            }
        }
    }
    
    settings["mcpServers"] = mcp_config
    
    # 备份原设置文件
    backup_path = cursor_settings_path.with_suffix('.json.backup')
    try:
        shutil.copy2(cursor_settings_path, backup_path)
        print(f"✓ 已备份原设置文件: {backup_path}")
    except Exception as e:
        print(f"⚠️  备份设置文件失败: {e}")
    
    # 写入新配置
    try:
        with open(cursor_settings_path, 'w', encoding='utf-8') as f:
            json.dump(settings, f, indent=2, ensure_ascii=False)
        print("✓ 已更新Cursor设置文件")
    except Exception as e:
        print(f"❌ 写入设置文件失败: {e}")
        return False
    
    print("\n🎉 Cursor MCP SSH工具配置完成！")
    print("\n📋 配置信息:")
    print(f"  服务器: 8.155.24.17")
    print(f"  用户: root")
    print(f"  端口: 22")
    print(f"  SSH工具路径: {ssh_tool_path}")
    
    print("\n⚠️  重要提醒:")
    print("1. 请重启Cursor编辑器以使配置生效")
    print("2. 重启后，您可以在Cursor中使用SSH工具")
    print("3. 如果遇到问题，请查看 CURSOR_MCP_SETUP.md")
    
    return True

def test_ssh_connection():
    """测试SSH连接"""
    print("\n🔍 测试SSH连接...")
    
    try:
        import subprocess
        import sys
        
        # 测试基本连接
        result = subprocess.run([
            sys.executable, "mcp_ssh_wrapper.py", "exec_command", "echo 'SSH连接测试成功'"
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✓ SSH连接测试成功")
            return True
        else:
            print(f"❌ SSH连接测试失败: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ SSH连接测试异常: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("Cursor MCP SSH工具自动配置")
    print("=" * 50)
    
    # 测试SSH连接
    if not test_ssh_connection():
        print("\n❌ SSH连接测试失败，请检查服务器配置")
        return
    
    # 设置Cursor MCP配置
    if setup_cursor_mcp():
        print("\n✅ 配置完成！请重启Cursor编辑器。")
    else:
        print("\n❌ 配置失败，请手动配置或查看错误信息。")

if __name__ == "__main__":
    main() 