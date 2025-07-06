# mcp-ssh-tool

一个基于MCP协议的远程SSH运维工具，支持通过标准输入输出与AI助手集成。

## 功能
- 远程执行任意命令
- 获取Docker容器列表
- 获取指定容器日志
- 完整的MCP工具集成支持

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 配置SSH连接
```bash
# 复制配置示例
cp config.example.json config.json
# 编辑配置文件，填入您的服务器信息
```

### 使用方法

#### 1. 直接使用SSH工具
```bash
# 执行命令
echo '{"action": "exec", "command": "ls /"}' | python3 mcp_ssh_tool.py

# 获取容器列表
echo '{"action": "list_containers"}' | python3 mcp_ssh_tool.py

# 获取容器日志
echo '{"action": "logs", "container": "docmost-docmost-1", "lines": 50}' | python3 mcp_ssh_tool.py
```

#### 2. 使用MCP包装器
```bash
# 执行命令
python3 mcp_ssh_wrapper.py exec_command "ls -la"

# 获取容器列表
python3 mcp_ssh_wrapper.py list_containers

# 获取容器日志
python3 mcp_ssh_wrapper.py get_container_logs "my-container" 50
```

#### 3. 集成到MCP工具系统
将 `mcp_ssh_tool.json` 添加到您的MCP配置中即可使用。

## MCP请求示例

### 执行命令
```json
{"action": "exec", "command": "ls /"}
```

### 获取容器列表
```json
{"action": "list_containers"}
```

### 获取容器日志
```json
{"action": "logs", "container": "docmost-docmost-1", "lines": 50}
```

## 配置方式
- 环境变量：SSH_HOST、SSH_USER、SSH_PASSWORD、SSH_PORT
- 或 config.json 文件

## 文档
- [安装指南](INSTALL.md) - 详细的安装和配置说明
- [MCP集成说明](MCP_INTEGRATION.md) - MCP工具集成指南

## 项目结构
```
mcp-ssh-tool/
├── mcp_ssh_tool.py          # 核心SSH工具
├── mcp_ssh_wrapper.py       # MCP工具包装器
├── mcp_ssh_tool.json        # MCP工具配置文件
├── mcp_tool_definition.json # 工具定义文件
├── config.example.json      # 配置示例
├── requirements.txt         # 依赖列表
├── README.md               # 项目说明
├── INSTALL.md              # 安装指南
└── MCP_INTEGRATION.md      # MCP集成说明
``` 