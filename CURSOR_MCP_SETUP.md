# Cursor MCP SSH工具集成指南

## 概述

本指南将帮助您将SSH工具集成到Cursor编辑器的MCP工具系统中。

## 服务器信息

- **主机**: YOUR_SERVER_IP
- **用户**: YOUR_USERNAME
- **密码**: YOUR_PASSWORD
- **端口**: 22

## 步骤1: 确认工具已准备就绪

确保SSH工具项目已正确设置：

```bash
cd /path/to/your/mcp-ssh-tool
source venv/bin/activate
```

## 步骤2: 测试SSH连接

在集成到Cursor之前，先测试SSH连接是否正常：

```bash
# 测试基本连接
python3 mcp_ssh_wrapper.py exec_command "echo 'SSH连接测试成功'"

# 测试获取系统信息
python3 mcp_ssh_wrapper.py exec_command "uname -a"

# 测试Docker容器列表
python3 mcp_ssh_wrapper.py list_containers
```

## 步骤3: 配置Cursor MCP

### 方法一: 使用Cursor设置

1. 打开Cursor编辑器
2. 按 `Cmd+,` 打开设置
3. 搜索 "MCP" 或 "Model Context Protocol"
4. 添加以下配置到设置中：

```json
{
  "mcpServers": {
    "ssh-tool": {
      "command": "python3",
      "args": ["/path/to/your/mcp-ssh-tool/mcp_ssh_tool.py"],
      "env": {
        "SSH_HOST": "YOUR_SERVER_IP",
        "SSH_USER": "YOUR_USERNAME",
        "SSH_PASSWORD": "YOUR_PASSWORD",
        "SSH_PORT": "22"
      }
    }
  }
}
```

### 方法二: 直接编辑配置文件

1. 打开Cursor设置文件：
```bash
open ~/Library/Application\ Support/Cursor/User/settings.json
```

2. 添加MCP配置：
```json
{
  "editor.fontFamily": "Consolas, 'JetBrains Mono', monospace",
  "window.commandCenter": 1,
  "redhat.telemetry.enabled": true,
  "mcpServers": {
    "ssh-tool": {
      "command": "python3",
      "args": ["/path/to/your/mcp-ssh-tool/mcp_ssh_tool.py"],
      "env": {
        "SSH_HOST": "YOUR_SERVER_IP",
        "SSH_USER": "YOUR_USERNAME",
        "SSH_PASSWORD": "YOUR_PASSWORD",
        "SSH_PORT": "22"
      }
    }
  }
}
```

## 步骤4: 重启Cursor

配置完成后，重启Cursor编辑器以使MCP配置生效。

## 步骤5: 验证集成

重启后，您可以在Cursor中使用以下功能：

### 在Cursor中测试SSH工具

1. 打开Cursor的聊天界面
2. 尝试以下命令：

```
请帮我连接到服务器并执行 ls -la 命令
```

```
请获取服务器上的Docker容器列表
```

```
请获取容器 my-container 的最近50行日志
```

## 可用工具

集成后，您可以在Cursor中使用以下SSH工具：

### 1. 执行命令
- **功能**: 在远程服务器上执行任意命令
- **示例**: `ls -la`, `ps aux`, `df -h`

### 2. 获取容器列表
- **功能**: 获取Docker容器列表
- **示例**: 查看所有运行中的容器

### 3. 获取容器日志
- **功能**: 获取指定容器的日志
- **参数**: 容器名称、日志行数

## 故障排除

### 常见问题

1. **MCP工具未加载**
   - 检查配置文件路径是否正确
   - 确认Python环境和依赖已安装
   - 重启Cursor编辑器

2. **SSH连接失败**
   - 检查服务器IP和端口
   - 验证用户名和密码
   - 确认服务器SSH服务正常运行

3. **权限错误**
   - 检查用户权限
   - 确认Docker访问权限

### 调试步骤

1. **检查工具状态**：
```bash
cd /path/to/your/mcp-ssh-tool
source venv/bin/activate
python3 mcp_ssh_wrapper.py list_containers
```

2. **查看Cursor日志**：
   - 打开Cursor
   - 按 `Cmd+Shift+P` 打开命令面板
   - 搜索 "Developer: Toggle Developer Tools"
   - 查看控制台错误信息

3. **测试SSH连接**：
```bash
ssh YOUR_USERNAME@YOUR_SERVER_IP
```

## 安全注意事项

1. **密码安全**: 当前配置使用明文密码，建议在生产环境中使用SSH密钥认证
2. **网络安全**: 确保SSH连接使用加密传输
3. **权限控制**: 限制SSH用户的权限范围
4. **日志记录**: 记录所有SSH操作日志

## 更新配置

如果需要更改服务器配置：

1. 编辑配置文件或环境变量
2. 更新Cursor设置中的环境变量
3. 重启Cursor编辑器

## 支持

如果遇到问题，请检查：
- SSH工具项目文档：`README.md`
- 安装指南：`INSTALL.md`
- MCP集成说明：`MCP_INTEGRATION.md` 