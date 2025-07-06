# MCP SSH工具集成说明

## 概述

这个项目提供了一个基于MCP（Model Context Protocol）协议的SSH运维工具，可以轻松集成到支持MCP的AI助手中。

## 文件说明

- `mcp_ssh_tool.py` - 核心SSH工具
- `mcp_ssh_wrapper.py` - MCP工具包装器
- `mcp_ssh_tool.json` - MCP工具配置文件
- `mcp_tool_definition.json` - 工具定义文件
- `config.example.json` - 配置示例

## 安装和配置

### 1. 安装依赖

```bash
# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置SSH连接

#### 方式一：环境变量
```bash
export SSH_HOST="your-server-ip"
export SSH_USER="your-username"
export SSH_PASSWORD="your-password"
export SSH_PORT="22"
```

#### 方式二：配置文件
复制 `config.example.json` 为 `config.json` 并修改：
```json
{
  "host": "your-server-ip",
  "user": "your-username", 
  "password": "your-password",
  "port": 22
}
```

## 使用方法

### 1. 直接使用SSH工具

```bash
# 执行命令
echo '{"action": "exec", "command": "ls -la"}' | python3 mcp_ssh_tool.py

# 获取容器列表
echo '{"action": "list_containers"}' | python3 mcp_ssh_tool.py

# 获取容器日志
echo '{"action": "logs", "container": "my-container", "lines": 50}' | python3 mcp_ssh_tool.py
```

### 2. 使用MCP包装器

```bash
# 执行命令
python3 mcp_ssh_wrapper.py exec_command "ls -la"

# 获取容器列表
python3 mcp_ssh_wrapper.py list_containers

# 获取容器日志
python3 mcp_ssh_wrapper.py get_container_logs "my-container" 50
```

### 3. 集成到MCP工具系统

将 `mcp_ssh_tool.json` 添加到您的MCP配置中：

```json
{
  "mcpServers": {
    "ssh-tool": {
      "command": "python3",
      "args": ["mcp_ssh_tool.py"],
      "env": {
        "SSH_HOST": "your-server-ip",
        "SSH_USER": "your-username",
        "SSH_PASSWORD": "your-password",
        "SSH_PORT": "22"
      }
    }
  }
}
```

## 支持的操作

### 1. 执行命令 (exec)
```json
{
  "action": "exec",
  "command": "ls -la /var/log"
}
```

### 2. 获取容器列表 (list_containers)
```json
{
  "action": "list_containers"
}
```

### 3. 获取容器日志 (logs)
```json
{
  "action": "logs",
  "container": "my-container",
  "lines": 100
}
```

## 响应格式

所有操作都返回统一的JSON响应格式：

```json
{
  "success": true,
  "output": "命令输出内容",
  "error": "错误信息（如果有）"
}
```

## 错误处理

工具包含完善的错误处理机制：

- SSH连接失败
- 命令执行错误
- 参数验证错误
- JSON格式错误

## 安全注意事项

1. **密码安全**：建议使用SSH密钥认证而非密码
2. **网络安全**：确保SSH连接使用加密传输
3. **权限控制**：限制SSH用户的权限范围
4. **日志记录**：记录所有SSH操作日志

## 故障排除

### 常见问题

1. **连接失败**
   - 检查服务器IP和端口
   - 验证用户名和密码
   - 确认SSH服务正常运行

2. **权限错误**
   - 检查用户权限
   - 确认Docker访问权限

3. **命令执行失败**
   - 检查命令语法
   - 验证命令路径

### 调试模式

启用详细日志输出：
```bash
export SSH_DEBUG=1
python3 mcp_ssh_tool.py
```

## 扩展功能

可以通过修改 `mcp_ssh_tool.py` 添加更多功能：

- 文件传输
- 进程管理
- 系统监控
- 备份操作

## 许可证

本项目采用MIT许可证。 