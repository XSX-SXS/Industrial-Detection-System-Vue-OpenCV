#!/usr/bin/env python3
# Google Colab部署脚本

import subprocess
import threading
import time
import os
import sys

# 颜色输出
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

def print_color(color, text):
    print(f"{color}{text}{Colors.RESET}")

def run_command(command, description="", shell=True, wait=True):
    """执行命令并显示结果"""
    if description:
        print_color(Colors.BLUE, f"\n{description}...")
    
    if wait:
        result = subprocess.run(command, shell=shell, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print_color(Colors.RED, result.stderr)
        return result.returncode
    else:
        process = subprocess.Popen(command, shell=shell)
        return process

def install_system_dependencies():
    """安装系统依赖"""
    run_command("apt-get update", "更新系统包列表")
    run_command("apt-get install -y libgl1-mesa-glx libx11-xcb1 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xkb1", "安装系统依赖")

def install_python_dependencies():
    """安装Python依赖"""
    run_command("pip install --upgrade pip", "更新pip")
    run_command("pip install -r requirements.txt", "安装项目Python依赖")
    run_command("pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118", "安装PyTorch")

def install_nodejs_and_frontend():
    """安装Node.js和前端依赖"""
    run_command("curl -fsSL https://deb.nodesource.com/setup_18.x | bash -", "安装Node.js 18")
    run_command("apt-get install -y nodejs", "安装Node.js包")
    run_command("node -v && npm -v", "验证Node.js和npm安装")
    run_command("npm install", "安装前端依赖")
    run_command("npm run build", "构建前端项目")

def setup_ngrok(auth_token):
    """设置ngrok"""
    run_command("pip install pyngrok", "安装pyngrok")
    
    # 设置ngrok认证令牌
    from pyngrok import ngrok
    ngrok.set_auth_token(auth_token)
    print_color(Colors.GREEN, "ngrok认证令牌设置成功")
    
    return ngrok

def start_backend_service():
    """启动后端服务"""
    print_color(Colors.BLUE, "\n启动后端服务...")
    backend_process = run_command(
        "python -m uvicorn src.backend.main:app --host 0.0.0.0 --port 8000",
        wait=False
    )
    
    # 等待服务启动
    time.sleep(5)
    return backend_process

def create_ngrok_tunnel(ngrok):
    """创建ngrok隧道"""
    print_color(Colors.BLUE, "创建ngrok隧道...")
    tunnel = ngrok.connect(addr="8000", proto="http")
    public_url = tunnel.public_url
    print_color(Colors.GREEN, f"\n✅ 后端服务已启动！")
    print_color(Colors.GREEN, f"API文档地址: {public_url}/docs")
    print_color(Colors.GREEN, f"前端访问地址: {public_url}")
    return tunnel

def main():
    """主函数"""
    print_color(Colors.GREEN, "=== 工业检测系统Google Colab部署脚本 ===")
    
    # 检查是否在Colab环境中
    if not os.path.exists("/content"):
        print_color(Colors.RED, "错误: 此脚本设计用于Google Colab环境")
        sys.exit(1)
    
    # 1. 安装系统依赖
    install_system_dependencies()
    
    # 2. 安装Python依赖
    install_python_dependencies()
    
    # 3. 安装Node.js和前端依赖
    install_nodejs_and_frontend()
    
    # 4. 设置ngrok
    auth_token = input("请输入您的ngrok认证令牌: ")
    if not auth_token:
        print_color(Colors.RED, "错误: ngrok认证令牌不能为空")
        sys.exit(1)
    
    ngrok = setup_ngrok(auth_token)
    
    # 5. 启动后端服务
    backend_process = start_backend_service()
    
    # 6. 创建ngrok隧道
    tunnel = create_ngrok_tunnel(ngrok)
    
    print_color(Colors.YELLOW, "\n⚠️ 注意事项:")
    print("1. Google Colab会话有12小时限制，会话结束后服务将停止")
    print("2. 系统默认不支持摄像头硬件访问")
    print("3. 如需持久化存储，请挂载Google Drive")
    
    # 保持脚本运行
    try:
        while True:
            time.sleep(3600)  # 每小时检查一次
    except KeyboardInterrupt:
        print_color(Colors.BLUE, "\n停止服务...")
        backend_process.terminate()
        ngrok.kill()
        print_color(Colors.GREEN, "服务已停止")

if __name__ == "__main__":
    main()
