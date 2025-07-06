#!/usr/bin/env python3
import sys
import json
import paramiko
import os

def load_config():
    # 优先环境变量，其次config.json
    config = {}
    config_path = os.environ.get('MCP_SSH_CONFIG', 'config.json')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
    config['host'] = os.environ.get('SSH_HOST', config.get('host', '127.0.0.1'))
    config['user'] = os.environ.get('SSH_USER', config.get('user', 'root'))
    config['password'] = os.environ.get('SSH_PASSWORD', config.get('password', ''))
    config['port'] = int(os.environ.get('SSH_PORT', config.get('port', 22)))
    return config

class SSHClient:
    def __init__(self, host, user, password, port=22):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.client = None

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            hostname=self.host,
            username=self.user,
            password=self.password,
            port=self.port,
            timeout=10
        )

    def exec_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        out = stdout.read().decode('utf-8')
        err = stderr.read().decode('utf-8')
        return out, err

    def close(self):
        if self.client:
            self.client.close()

if __name__ == "__main__":
    config = load_config()
    ssh = SSHClient(config['host'], config['user'], config['password'], config['port'])
    try:
        ssh.connect()
        while True:
            line = sys.stdin.readline()
            if not line:
                break
            try:
                req = json.loads(line)
                action = req.get('action')
                if action == 'exec':
                    command = req.get('command')
                    if not command:
                        resp = {"success": False, "error": "No command provided"}
                    else:
                        out, err = ssh.exec_command(command)
                        resp = {"success": True, "output": out, "error": err}
                elif action == 'list_containers':
                    out, err = ssh.exec_command('docker ps')
                    resp = {"success": True, "output": out, "error": err}
                elif action == 'logs':
                    container = req.get('container')
                    lines = req.get('lines', 100)
                    if not container:
                        resp = {"success": False, "error": "No container provided"}
                    else:
                        out, err = ssh.exec_command(f'docker logs --tail {lines} {container}')
                        resp = {"success": True, "output": out, "error": err}
                else:
                    resp = {"success": False, "error": "Unknown action"}
            except Exception as e:
                resp = {"success": False, "error": str(e)}
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + '\n')
            sys.stdout.flush()
    finally:
        ssh.close() 