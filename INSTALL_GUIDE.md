# 工业检测系统安装指南

## Python环境配置状态

✅ 已完成：
- ✅ 创建Python虚拟环境：`yolo-detect`
- ✅ 激活虚拟环境
- ✅ 升级pip到最新版本 (25.3)
- ✅ 安装所有Python依赖 (requirements.txt)
- ✅ 后端服务已启动并运行在 http://127.0.0.1:8000

## 接下来需要完成的步骤

### 1. 安装Node.js

您的系统上尚未安装Node.js，需要先安装：

### 方法1：使用Homebrew（推荐）

#### 步骤1：安装Homebrew（如果尚未安装）
打开终端并运行以下命令：
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 步骤2：使用Homebrew安装Node.js
```bash
brew install node
```

### 方法2：直接安装

访问Node.js官方网站下载安装包：
- 网址：https://nodejs.org/zh-cn/download/
- 选择macOS安装包
- 双击安装包并按照提示完成安装

### 验证Node.js安装

安装完成后，运行以下命令验证：
```bash
node -v
npm -v
```

### 2. 安装前端依赖

在终端中进入项目目录：
```bash
cd /Applications/工作文件/Industrial-Detection-System-Vue-OpenCV-master
```

安装前端依赖：
```bash
npm install
```

### 3. 启动前端服务

```bash
npm run dev
```

前端服务将在默认端口（通常是5173）运行

### 4. 访问系统

- 前端开发服务器：http://localhost:5173
- 后端API服务：http://127.0.0.1:8000

## 摄像头权限说明

从后端日志可以看到，系统检测到了摄像头，但需要您授予相机访问权限：

**macOS相机权限设置：**
1. 打开「系统偏好设置」→「安全性与隐私」→「隐私」→「相机」
2. 确保您使用的终端应用（如Terminal或iTerm2）已被勾选
3. 如果没有看到终端应用，可以点击左下角的「+」按钮添加
4. 重启后端服务使权限生效

## 系统功能

1. **实时视频流预览与检测**
2. **数据标注**
3. **图像处理流水线**
4. **模型调用**
5. **实时监控**

## 故障排除

### 端口被占用
如果后端服务无法启动，可以尝试更改端口：
```bash
python -m uvicorn src.backend.main:app --reload --port 8001
```

### 依赖安装失败
尝试清理并重新安装：
```bash
rm -rf node_modules package-lock.json
npm install
```

### 前端无法连接后端
检查CORS配置，确保后端允许前端访问。