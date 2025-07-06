# MCP SSH工具安装指南

## 快速开始

### 1. 环境准备

确保您的系统已安装Python 3.7+和pip：

```bash
python3 --version
pip3 --version
```

### 2. 克隆项目

```bash
git clone <your-repo-url>
cd mcp-ssh-tool
```

### 3. 安装依赖

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 4. 配置SSH连接

#### 方法一：使用配置文件

```bash
# 复制配置示例
cp config.example.json config.json

# 编辑配置文件
nano config.json
```

配置文件内容：
```json
{
  "host": "your-server-ip",
  "user": "your-username",
  "password": "your-password",
  "port": 22
}
```

#### 方法二：使用环境变量

```bash
export SSH_HOST="your-server-ip"
export SSH_USER="your-username"
export SSH_PASSWORD="your-password"
export SSH_PORT="22"
```

### 5. 测试连接

```bash
# 测试基本功能
python3 mcp_ssh_wrapper.py exec_command "echo 'Hello World'"

# 测试容器列表
python3 mcp_ssh_wrapper.py list_containers
```

## 集成到MCP系统

### 1. 添加到MCP配置

将以下配置添加到您的MCP工具配置文件中：

```json
{
  "mcpServers": {
    "ssh-tool": {
      "command": "python3",
      "args": ["/path/to/mcp-ssh-tool/mcp_ssh_tool.py"],
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

### 2. 工具定义

工具支持以下操作：

- `exec_command` - 执行任意命令
- `list_containers` - 获取Docker容器列表
- `get_container_logs` - 获取容器日志

### 3. 使用示例

```bash
# 执行命令
python3 mcp_ssh_wrapper.py exec_command "ls -la /var/log"

# 获取容器列表
python3 mcp_ssh_wrapper.py list_containers

# 获取容器日志
python3 mcp_ssh_wrapper.py get_container_logs "my-container" 50
```

## 故障排除

### 常见问题

1. **SSH连接失败**
   ```
   错误: [Errno None] Unable to connect to port 22
   ```
   解决方案：
   - 检查服务器IP和端口
   - 确认SSH服务运行
   - 验证防火墙设置

2. **认证失败**
   ```
   错误: Authentication failed
   ```
   解决方案：
   - 检查用户名和密码
   - 确认用户有SSH登录权限
   - 考虑使用SSH密钥认证

3. **权限错误**
   ```
   错误: Permission denied
   ```
   解决方案：
   - 检查用户权限
   - 确认Docker访问权限
   - 使用sudo（如果允许）

### 调试模式

启用详细日志：

```bash
export SSH_DEBUG=1
python3 mcp_ssh_tool.py
```

### 日志文件

查看详细错误信息：

```bash
# 查看SSH连接日志
tail -f /var/log/auth.log  # Linux
tail -f /var/log/secure    # CentOS/RHEL
```

## 安全建议

1. **使用SSH密钥认证**
   ```bash
   # 生成SSH密钥
   ssh-keygen -t rsa -b 4096
   
   # 复制公钥到服务器
   ssh-copy-id user@server
   ```

2. **限制SSH用户权限**
   ```bash
   # 在服务器上创建受限用户
   sudo useradd -m -s /bin/bash sshuser
   sudo usermod -aG docker sshuser
   ```

3. **配置SSH安全选项**
   ```bash
   # 编辑SSH配置
   sudo nano /etc/ssh/sshd_config
   
   # 禁用密码认证
   PasswordAuthentication no
   
   # 限制用户登录
   AllowUsers sshuser
   ```

## 性能优化

1. **连接池**
   - 工具会自动管理SSH连接
   - 避免频繁建立/断开连接

2. **超时设置**
   - 默认连接超时：10秒
   - 可在代码中调整

3. **并发控制**
   - 当前版本为单线程
   - 可根据需要扩展为多线程

## 扩展开发

### 添加新功能

1. 在 `mcp_ssh_tool.py` 中添加新的action
2. 在 `mcp_ssh_wrapper.py` 中添加对应的方法
3. 更新 `mcp_tool_definition.json` 中的工具定义

### 示例：添加文件传输功能

```python
# 在 mcp_ssh_tool.py 中添加
elif action == 'upload_file':
    local_path = req.get('local_path')
    remote_path = req.get('remote_path')
    if not local_path or not remote_path:
        resp = {"success": False, "error": "Missing file paths"}
    else:
        # 实现文件上传逻辑
        resp = {"success": True, "output": "File uploaded"}
```

## 支持

- 项目文档：`README.md`
- 集成说明：`MCP_INTEGRATION.md`
- 问题反馈：GitHub Issues

## 许可证

MIT License - 详见 LICENSE 文件 