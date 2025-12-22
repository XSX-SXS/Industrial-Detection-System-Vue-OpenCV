# 工业检测系统Google Colab部署指南

## 注意事项

1. **Google Colab限制**：
   - 免费版Colab有12小时的运行时间限制
   - 计算资源有限，可能会影响模型性能
   - 不支持长时间后台运行服务
   - 需要定期重新连接会话

2. **环境限制**：
   - Colab默认不支持摄像头硬件访问
   - 需要使用ngrok等工具进行端口转发
   - 前端部署需要特殊处理

## 部署步骤

### 步骤1：准备工作

1. **克隆项目到Colab**
   ```python
   # 在Colab的代码单元格中运行
   !git clone <项目仓库地址>
   %cd Industrial-Detection-System-Vue-OpenCV-master
   ```

2. **安装系统依赖**
   ```python
   !apt-get update
   !apt-get install -y libgl1-mesa-glx libx11-xcb1 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xkb1
   ```

### 步骤2：安装Python依赖

```python
# 安装基础依赖
!pip install -r requirements.txt

# 安装PyTorch（如果requirements.txt中的版本在Colab中不兼容）
!pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 步骤3：安装Node.js和前端依赖

```python
# 安装Node.js
!curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
!apt-get install -y nodejs

# 验证Node.js和npm
!node -v
!npm -v

# 安装前端依赖
!npm install

# 构建前端项目
!npm run build
```

### 步骤4：配置ngrok进行端口转发

1. **安装ngrok**
   ```python
   !pip install pyngrok
   ```

2. **设置ngrok认证令牌**
   - 访问 [ngrok官网](https://ngrok.com/) 注册账号
   - 在"Your Authtoken"页面获取认证令牌
   ```python
   from pyngrok import ngrok
   ngrok.set_auth_token("YOUR_NGROK_AUTH_TOKEN")
   ```

### 步骤5：启动后端服务

```python
# 导入必要的库
import subprocess
import threading
import time
from pyngrok import ngrok
import requests

# 启动FastAPI后端服务
backend_process = subprocess.Popen([
    "python", "-m", "uvicorn", "src.backend.main:app", 
    "--host", "0.0.0.0", "--port", "8000"
])

# 等待服务启动
print("正在启动后端服务...")
time.sleep(5)

# 使用ngrok创建隧道
http_tunnel = ngrok.connect(addr="8000", proto="http")
print(f"后端服务已启动！访问地址：{http_tunnel.public_url}")

# 验证服务是否正常运行
try:
    response = requests.get(f"{http_tunnel.public_url}/docs")
    if response.status_code == 200:
        print("✓ FastAPI文档可访问")
    else:
        print("✗ FastAPI服务可能存在问题")
except Exception as e:
    print(f"✗ 无法访问FastAPI服务：{str(e)}")
```

### 步骤6：访问系统

1. **API文档**：`{ngrok_url}/docs`
2. **前端页面**：`{ngrok_url}`

## 高级配置

### 1. 使用自定义域名

如果有自己的域名，可以在ngrok中配置：

```python
from pyngrok import ngrok

# 设置自定义域名
tunnel = ngrok.connect(
    addr="8000",
    proto="http",
    hostname="your-domain.ngrok-free.app"
)
```

### 2. 配置持久化存储

```python
# 挂载Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 创建软链接到项目目录
!ln -s /content/drive/MyDrive/industrial-detection/models /content/Industrial-Detection-System-Vue-OpenCV-master/models
!ln -s /content/drive/MyDrive/industrial-detection/data /content/Industrial-Detection-System-Vue-OpenCV-master/data
```

### 3. 优化性能

```python
# 使用GPU加速（如果可用）
import torch
print(f"CUDA可用: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU设备: {torch.cuda.get_device_name(0)}")

# 配置模型使用GPU
# 在src/backend/services/model.py中修改模型加载代码
```

## 常见问题解决

### 问题1：依赖安装失败

```python
# 尝试更新pip
!pip install --upgrade pip

# 单独安装问题依赖
!pip install <问题依赖包> --force-reinstall
```

### 问题2：端口被占用

```python
# 查找占用端口的进程
!lsof -i :8000

# 终止进程
!kill -9 <PID>
```

### 问题3：ngrok连接失败

```python
# 重新连接ngrok
ngrok.kill()
time.sleep(2)
new_tunnel = ngrok.connect(addr="8000", proto="http")
```

### 问题4：前端页面无法访问

```python
# 检查前端构建是否成功
!ls -la dist/

# 检查CORS配置
# 在src/backend/main.py中确保CORS配置正确
```

## 资源管理

1. **定期保存模型和数据**
   ```python
   # 将模型保存到Google Drive
   !cp -r models/ /content/drive/MyDrive/industrial-detection/
   !cp -r data/ /content/drive/MyDrive/industrial-detection/
   ```

2. **清理资源**
   ```python
   # 终止后端服务
   backend_process.terminate()

   # 关闭ngrok隧道
   ngrok.kill()

   # 清理内存
   import gc
   gc.collect()
   ```

## 注意事项

1. **会话限制**：
   - Colab会话会在一段时间不活动后断开
   - 建议设置会话自动重连

2. **资源限制**：
   - 免费版Colab的GPU内存有限
   - 大模型可能无法运行或运行缓慢

3. **安全考虑**：
   - 不要在Colab中存储敏感数据
   - 使用ngrok时注意保护隧道URL

## 替代方案

如果需要长期稳定运行，建议考虑：
1. **Google Cloud Platform**
2. **AWS EC2**
3. **腾讯云/阿里云**
4. **本地服务器部署**

## 联系支持

如果在部署过程中遇到问题，请参考项目文档或联系技术支持。