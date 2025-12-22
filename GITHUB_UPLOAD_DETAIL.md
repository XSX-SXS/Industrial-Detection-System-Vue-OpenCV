# GitHub上传详细指南

## 一、在GitHub上创建仓库

### 步骤1：登录GitHub账号

1. 打开浏览器访问 [GitHub官网](https://github.com/)
2. 输入您的用户名/邮箱和密码进行登录

### 步骤2：创建新仓库

1. 登录成功后，点击右上角的"+"图标
2. 在下拉菜单中选择"New repository"

### 步骤3：填写仓库信息

在创建仓库页面，您需要填写以下信息：

| 字段 | 说明 | 示例值 |
|------|------|--------|
| Repository name | 仓库名称 | Industrial-Detection-System-Vue-OpenCV |
| Description | 仓库描述（可选） | 工业检测系统Vue+OpenCV实现 |
| Visibility | 仓库可见性 | Public（公开）或Private（私有） |

### 步骤4：完成创建

1. **不要勾选**以下选项（因为我们的项目中已经包含了这些文件）：
   - Initialize this repository with a README
   - Add .gitignore
   - Choose a license

2. 点击页面底部的"Create repository"按钮

### 步骤5：获取仓库URL

创建成功后，您将看到一个新的页面，显示仓库的基本信息。

在页面中找到"Quick setup"部分：
- 选择"HTTPS"或"SSH"选项卡
- 复制显示的URL地址

示例HTTPS URL：`https://github.com/your-username/Industrial-Detection-System-Vue-OpenCV.git`
示例SSH URL：`git@github.com:your-username/Industrial-Detection-System-Vue-OpenCV.git`

## 二、将本地项目推送到GitHub

### 步骤1：添加远程仓库

在终端中运行以下命令，将本地仓库与GitHub仓库关联：

```bash
# 使用HTTPS连接
git remote add origin https://github.com/XSX-SXS/Industrial-Detection-System-Vue-OpenCV.git

# 或使用SSH连接
git remote add origin git@github.com:your-username/Industrial-Detection-System-Vue-OpenCV.git
```

**命令解释**：
- `git remote add`：添加远程仓库
- `origin`：远程仓库的别名（可以自定义，通常使用origin）
- `URL`：GitHub仓库的URL地址

### 步骤2：检查远程仓库配置

```bash
git remote -v
```

您将看到类似以下的输出：
```
origin  https://github.com/your-username/Industrial-Detection-System-Vue-OpenCV.git (fetch)
origin  https://github.com/your-username/Industrial-Detection-System-Vue-OpenCV.git (push)
```

### 步骤3：推送代码

```bash
git push -u origin main
```

**命令解释**：
- `git push`：将本地代码推送到远程仓库
- `-u`：设置上游分支，后续推送可以简化为`git push`
- `origin`：远程仓库别名
- `main`：本地分支名称（如果您的默认分支是master，请使用master）

## 三、常见问题及解决方法

### 问题1：推送失败 - 权限被拒绝

**错误信息示例**：
```
remote: Permission to your-username/repository.git denied to user.
fatal: unable to access 'https://github.com/your-username/repository.git/': The requested URL returned error: 403
```

**解决方法**：

#### 方法1：使用个人访问令牌（HTTPS）

##### 步骤1：生成个人访问令牌

1. 登录GitHub，点击右上角头像 → **Settings**
2. 在左侧菜单中，点击 **Developer settings**（页面底部）
3. 在左侧菜单中，点击 **Personal access tokens** → **Tokens (classic)**
4. 点击 **Generate new token** 按钮
5. 在 **Note** 字段中，输入一个描述性名称（例如："工业检测系统项目"）
6. 在 **Expiration** 字段中，选择令牌的有效期（建议选择短期有效，例如30天）
7. 在 **Select scopes** 部分，勾选以下权限：
   - **repo**：所有仓库权限（必须勾选）
     - repo:status
     - repo_deployment
     - public_repo
     - repo:invite
   - **workflow**：如果项目使用GitHub Actions（可选）
8. 点击页面底部的 **Generate token** 按钮
9. **重要**：复制生成的令牌并妥善保存，因为您将无法再次查看完整令牌！

##### 步骤2：使用令牌进行认证

**方法A：在远程URL中直接使用令牌**
```bash
# 设置带有令牌的远程仓库URL
git remote add origin https://your-username:your-personal-access-token@github.com/your-username/Industrial-Detection-System-Vue-OpenCV.git

# 如果已经设置了远程仓库，可以更新URL
git remote set-url origin https://your-username:your-personal-access-token@github.com/your-username/Industrial-Detection-System-Vue-OpenCV.git
```

**方法B：在Git配置中存储凭据**

在macOS上：
```bash
# 配置Git使用系统钥匙串存储凭据
git config --global credential.helper osxkeychain

# 首次推送时，系统会提示输入用户名和令牌
# 令牌将被存储在钥匙串中，后续推送无需再次输入
```

在Windows上：
```bash
# 配置Git使用Windows凭据管理器
git config --global credential.helper manager-core

# 首次推送时，系统会弹出窗口提示输入用户名和令牌
# 令牌将被存储，后续推送无需再次输入
```

在Linux上：
```bash
# 配置Git使用存储助手
git config --global credential.helper store

# 首次推送时，系统会提示输入用户名和令牌
# 令牌将被存储在~/.git-credentials文件中
```

##### 步骤3：测试连接

```bash
# 推送测试
git push -u origin main

# 如果配置正确，推送应该成功完成
```

#### 方法2：使用SSH连接

##### 步骤1：生成SSH密钥对

**在macOS/Linux上：**
```bash
# 生成4096位RSA密钥对
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# 系统提示保存位置，默认 ~/.ssh/id_rsa，直接按Enter确认
# 系统提示设置密码短语(Passphrase)，建议设置一个强密码短语以提高安全性
# 再次输入密码短语确认
```

**在Windows上（使用Git Bash或PowerShell）：**
```bash
# 生成4096位RSA密钥对
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"

# 按Enter确认保存位置，默认 C:\Users\YourUsername\.ssh\id_rsa
# 设置密码短语并确认
```

##### 步骤2：查看公钥内容

**在macOS/Linux上：**
```bash
cat ~/.ssh/id_rsa.pub
```

**在Windows上（使用Git Bash）：**
```bash
cat ~/.ssh/id_rsa.pub
```

**在Windows上（使用PowerShell）：**
```powershell
Get-Content ~/.ssh/id_rsa.pub
```

##### 步骤3：在GitHub上添加公钥

1. 登录GitHub，点击右上角头像 → **Settings**
2. 在左侧菜单中，点击 **SSH and GPG keys**
3. 点击 **New SSH key** 按钮
4. 在 **Title** 字段中，输入一个描述性名称（例如："My MacBook Pro" 或 "Work PC"）
5. 在 **Key** 字段中，粘贴您刚刚复制的公钥内容
6. 点击 **Add SSH key** 按钮
7. 系统可能会要求您输入GitHub密码进行确认

##### 步骤4：测试SSH连接

在终端中运行以下命令测试连接：
```bash
ssh -T git@github.com
```

- 如果是首次连接，系统会提示确认GitHub的主机指纹：
  ```
  The authenticity of host 'github.com (192.30.255.112)' can't be established.
  RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
  Are you sure you want to continue connecting (yes/no)?
  ```
- 输入 `yes` 并按Enter
- 如果设置了密码短语，系统会提示输入密码短语
- 成功连接后，您会看到类似以下的提示：
  ```
  Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
  ```

##### 步骤5：使用SSH URL设置远程仓库

```bash
# 使用SSH URL连接远程仓库
git remote add origin git@github.com:your-username/Industrial-Detection-System-Vue-OpenCV.git
```

### 问题2：推送失败 - 分支不存在

**错误信息示例**：
```
fatal: The current branch main has no upstream branch.
```

**解决方法**：

1. 确保本地分支名称正确：
   ```bash
git branch
   ```

2. 如果分支名称不是main或master，创建或切换到正确的分支：
   ```bash
   # 创建并切换到main分支
git checkout -b main
   ```

3. 再次推送：
   ```bash
git push -u origin main
   ```

### 问题3：推送失败 - 本地分支与远程分支不同步

**错误信息示例**：
```
fatal: refusing to merge unrelated histories
```

**解决方法**：

```bash
# 强制推送（会覆盖远程仓库内容，谨慎使用）
git push -u origin main --force
```

### 问题4：推送速度慢

**解决方法**：

1. 使用SSH连接替代HTTPS
2. 使用`--depth 1`参数克隆（仅克隆最近一次提交）
3. 检查网络连接

## 四、高级操作

### 查看提交历史

```bash
git log
```

### 创建新分支

```bash
# 创建并切换到新分支
git checkout -b feature/new-feature

# 推送新分支到远程仓库
git push -u origin feature/new-feature
```

### 合并分支

```bash
# 切换到目标分支
git checkout main

# 合并其他分支
git merge feature/new-feature
```

### 撤销提交

```bash
# 撤销最近一次提交，但保留修改
git reset HEAD~1

# 撤销最近一次提交，同时删除修改
git reset --hard HEAD~1
```

## 五、完整命令流程

```bash
# 1. 初始化Git仓库
git init

# 2. 检查当前目录状态
git status

# 3. 添加所有文件到暂存区
git add .

# 4. 配置用户信息
git config user.name "Your Name"
git config user.email "your.email@example.com"

# 5. 提交文件
git commit -m "Initial commit"

# 6. 添加远程仓库
git remote add origin https://github.com/your-username/Industrial-Detection-System-Vue-OpenCV.git

# 7. 检查远程仓库配置
git remote -v

# 8. 推送代码
git push -u origin main
```

## 六、图形化工具推荐

如果您更喜欢使用图形化工具，可以考虑以下选项：

1. **GitHub Desktop**：GitHub官方提供的桌面客户端
2. **SourceTree**：Atlassian提供的免费Git客户端
3. **GitKraken**：功能强大的Git客户端，有免费和付费版本

这些工具可以简化Git操作，适合初学者使用。