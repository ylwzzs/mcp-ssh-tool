#!/usr/bin/env python3
"""
MCP SSH工具包装器
将SSH工具包装成标准的MCP工具格式
"""

import json
import sys
import subprocess
import os
from typing import Dict, Any, Optional

class MCPSSHWrapper:
    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.ssh_process = None
        
    def load_config(self) -> Dict[str, Any]:
        """加载SSH配置"""
        config = {}
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                config = json.load(f)
        
        # 环境变量优先级更高
        config['host'] = os.environ.get('SSH_HOST', config.get('host', '127.0.0.1'))
        config['user'] = os.environ.get('SSH_USER', config.get('user', 'root'))
        config['password'] = os.environ.get('SSH_PASSWORD', config.get('password', ''))
        config['port'] = int(os.environ.get('SSH_PORT', config.get('port', 22)))
        
        return config
    
    def start_ssh_process(self):
        """启动SSH工具进程"""
        if self.ssh_process is None:
            self.ssh_process = subprocess.Popen(
                [sys.executable, 'mcp_ssh_tool.py'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
    
    def stop_ssh_process(self):
        """停止SSH工具进程"""
        if self.ssh_process:
            self.ssh_process.terminate()
            self.ssh_process.wait(timeout=5)
            self.ssh_process = None
    
    def send_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """发送请求到SSH工具"""
        try:
            self.start_ssh_process()
            
            # 发送请求
            request_json = json.dumps(request) + '\n'
            self.ssh_process.stdin.write(request_json)
            self.ssh_process.stdin.flush()
            
            # 读取响应
            response_line = self.ssh_process.stdout.readline()
            if response_line:
                return json.loads(response_line)
            else:
                return {"success": False, "error": "No response from SSH tool"}
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def exec_command(self, command: str) -> Dict[str, Any]:
        """执行命令"""
        request = {"action": "exec", "command": command}
        return self.send_request(request)
    
    def list_containers(self) -> Dict[str, Any]:
        """获取容器列表"""
        request = {"action": "list_containers"}
        return self.send_request(request)
    
    def get_container_logs(self, container: str, lines: int = 100) -> Dict[str, Any]:
        """获取容器日志"""
        request = {"action": "logs", "container": container, "lines": lines}
        return self.send_request(request)

def main():
    """主函数 - MCP工具入口点"""
    if len(sys.argv) < 2:
        print("用法: python mcp_ssh_wrapper.py <tool_name> [args...]")
        sys.exit(1)
    
    tool_name = sys.argv[1]
    wrapper = MCPSSHWrapper()
    
    try:
        if tool_name == "exec_command":
            if len(sys.argv) < 3:
                print("错误: 需要提供命令")
                sys.exit(1)
            command = sys.argv[2]
            result = wrapper.exec_command(command)
            
        elif tool_name == "list_containers":
            result = wrapper.list_containers()
            
        elif tool_name == "get_container_logs":
            if len(sys.argv) < 3:
                print("错误: 需要提供容器名称")
                sys.exit(1)
            container = sys.argv[2]
            lines = int(sys.argv[3]) if len(sys.argv) > 3 else 100
            result = wrapper.get_container_logs(container, lines)
            
        else:
            print(f"错误: 未知工具 '{tool_name}'")
            sys.exit(1)
        
        # 输出结果
        print(json.dumps(result, ensure_ascii=False, indent=2))
        
    except Exception as e:
        print(json.dumps({"success": False, "error": str(e)}, ensure_ascii=False))
        sys.exit(1)
    finally:
        wrapper.stop_ssh_process()

if __name__ == "__main__":
    main() 