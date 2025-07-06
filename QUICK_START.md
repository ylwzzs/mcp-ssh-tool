# 🚀 SSH工具快速开始指南

## ✅ 配置已完成！

您的SSH工具已成功集成到Cursor编辑器中。

### 📋 服务器信息
- **主机**: YOUR_SERVER_IP
- **用户**: YOUR_USERNAME
- **端口**: 22

### 🔧 已配置的功能
- ✅ 远程命令执行
- ✅ Docker容器管理
- ✅ 容器日志查看

## 🎯 下一步操作

### 1. 重启Cursor编辑器
关闭并重新打开Cursor编辑器，使MCP配置生效。

### 2. 在Cursor中测试SSH工具

重启后，您可以在Cursor的聊天界面中使用以下命令：

#### 执行系统命令
```
请帮我连接到服务器并执行 ls -la 命令
```

#### 查看Docker容器
```
请获取服务器上的Docker容器列表
```

#### 查看容器日志
```
请获取 docmost-docmost-1 容器的最近50行日志
```

#### 系统信息
```
请帮我查看服务器的系统信息
```

#### 磁盘使用情况
```
请检查服务器的磁盘使用情况
```

## 🛠️ 可用工具

### 1. 执行命令 (exec_command)
- **功能**: 在远程服务器上执行任意命令
- **示例**: 
  - `ls -la` - 查看文件列表
  - `ps aux` - 查看进程
  - `df -h` - 查看磁盘使用
  - `free -h` - 查看内存使用

### 2. 获取容器列表 (list_containers)
- **功能**: 获取所有Docker容器状态
- **输出**: 容器ID、镜像、状态、端口映射等

### 3. 获取容器日志 (get_container_logs)
- **功能**: 获取指定容器的日志
- **参数**: 
  - 容器名称 (必需)
  - 日志行数 (可选，默认100行)

## 🔍 当前服务器状态

根据测试，您的服务器上运行着以下服务：

### Docker容器
- **docmost-docmost-1** - DocMost应用 (端口3000)
- **docmost-db-1** - PostgreSQL数据库
- **docmost-redis-1** - Redis缓存
- **dify_v140_mytech-*** - Dify AI平台相关服务
- **nginx** - Web服务器 (端口8088)

### 系统信息
- **操作系统**: Ubuntu Linux
- **内核版本**: 6.8.0-57-generic
- **架构**: x86_64

## 🚨 故障排除

### 如果工具不工作：

1. **检查Cursor是否重启**
   - 确保完全关闭并重新打开Cursor

2. **验证SSH连接**
   ```bash
   cd /Users/Duo/WPS\ 云文档/MytechCode/mcp-ssh-tool
   source venv/bin/activate
   python3 mcp_ssh_wrapper.py exec_command "echo test"
   ```

3. **查看Cursor日志**
   - 按 `Cmd+Shift+P`
   - 搜索 "Developer: Toggle Developer Tools"
   - 查看控制台错误信息

### 常见问题

**Q: 工具没有响应**
A: 请重启Cursor编辑器

**Q: SSH连接失败**
A: 检查服务器是否在线，网络是否正常

**Q: 权限错误**
A: 确认用户有执行相应命令的权限

## 📞 支持

如果遇到问题：
1. 查看 `CURSOR_MCP_SETUP.md` 详细设置指南
2. 查看 `INSTALL.md` 安装和故障排除
3. 运行 `python3 setup_cursor_mcp.py` 重新配置

## 🎉 开始使用！

现在您可以在Cursor中直接与远程服务器交互了！

尝试在Cursor聊天中输入：
```
请帮我查看服务器的运行状态
``` 