# Node.js详细安装指南（macOS）

## 方法1：使用Homebrew安装（推荐）

### 步骤1：安装Homebrew

如果您还没有安装Homebrew，请按照以下步骤安装：

1. 打开终端应用
2. 复制并粘贴以下命令，然后按回车键：
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

3. 按照终端中的提示完成安装
   - 您可能需要输入密码
   - 安装过程可能需要几分钟时间

### 步骤2：验证Homebrew安装

安装完成后，运行以下命令验证：
```bash
brew --version
```

如果安装成功，您将看到Homebrew的版本信息。

### 步骤3：使用Homebrew安装Node.js

运行以下命令安装Node.js：
```bash
brew install node
```

### 步骤4：验证Node.js安装

安装完成后，运行以下命令验证：
```bash
node -v
npm -v
```

如果安装成功，您将看到Node.js和npm的版本信息。

## 方法2：直接从官方网站下载安装

### 步骤1：下载Node.js安装包

1. 打开浏览器访问：https://nodejs.org/zh-cn/download/
2. 在"macOS安装包"部分，点击"64位"按钮下载安装包

### 步骤2：安装Node.js

1. 找到下载的安装包（通常在"下载"文件夹中）
2. 双击安装包文件
3. 按照安装向导的提示完成安装
   - 点击"继续"直到安装完成

### 步骤3：验证Node.js安装

1. 打开终端应用
2. 运行以下命令验证：
```bash
node -v
npm -v
```

如果安装成功，您将看到Node.js和npm的版本信息。

## 故障排除

### 情况1：命令仍然无法找到

如果安装完成后，运行`node -v`或`npm -v`仍然显示"command not found"，请尝试以下方法：

1. 关闭当前终端窗口，重新打开一个新的终端窗口
2. 检查Node.js是否正确安装在系统中：
   ```bash
   which node
   which npm
   ```
   
   如果显示路径，说明安装成功但环境变量可能需要配置

3. 配置环境变量（如果需要）：
   ```bash
   # 将以下内容添加到~/.zshrc文件中
   echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
   # 或者如果使用bash
   echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
   
   # 重新加载配置
   source ~/.zshrc
   # 或者如果使用bash
   source ~/.bash_profile
   ```

### 情况2：Homebrew安装失败

如果Homebrew安装失败，请尝试以下方法：

1. 检查网络连接
2. 确保您的macOS版本符合要求（至少需要macOS 10.14或更高版本）
3. 尝试手动安装Xcode命令行工具：
   ```bash
   xcode-select --install
   ```
4. 再次尝试安装Homebrew

## 安装完成后

Node.js安装完成后，您可以继续安装前端依赖：

```bash
# 进入项目目录
cd /Applications/工作文件/Industrial-Detection-System-Vue-OpenCV-master

# 安装前端依赖
npm install

# 启动前端服务
npm run dev
```

## 联系支持

如果您在安装过程中遇到任何问题，请随时联系技术支持或参考官方文档。