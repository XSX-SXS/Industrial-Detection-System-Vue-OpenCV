# 工业低代码计算机视觉系统

原始文献链接：https://mp.weixin.qq.com/s/SHFpFBWoQCOPrXFHkTYOMg?exptype=unsubscribed_card_recommend_article_u2i_mainprocess_coarse_sort_tlfeeds&ranksessionid=1765431118_1&req_id=1765416188536733&scene=169&subscene=200&sessionid=1765431118&flutter_pos=5&clicktime=1765431134&enterid=1765431134&finder_biz_enter_id=5&jumppath=1001_1765430980273,1102_1765431098035,1001_1765431114327,50094_1765431118381&jumppathdepth=4&ascene=56&fasttmpl_type=0&fasttmpl_fullversion=8035353-zh_CN-zip&fasttmpl_flag=0&realreporttime=1765431134063&devicetype=android-31&version=28004236&nettype=WIFI&abtest_cookie=AAACAA==&lang=zh_CN&session_us=gh_2d1a86caf781&countrycode=CN&exportkey=n_ChQIAhIQDnt+VHVNtNdPYQWkCSgWjxLxAQIE97dBBAEAAAAAADCOAyG5o88AAAAOpnltbLcz9gKNyK89dVj0pjwHe2dFhfiFO0CwBEQxBTagnRQ6ha83p5rUwqoG7TeQGlAoZC8H+APj3Mw2EgS+PDhbWy2bR/PL09CxfImGMJieZvlH+PfdoTBAwZ6wsQ3ZnI1D+amLR6TbvGdI3335r7VYGctTBI4PiPBUcQh3Ja0dpxpzo4kEOPgW1tqnoAKzGObf9gfkXTsM85oIFB98A+MWOeUTMaTLugLJPtRO6QqkY0+IsDT+PZG4LyzrCvFX8HeBfVfCgP7NGALz6reqdJGZCnZmF+i9NpQ=&pass_ticket=t+dCpVmRRwMTzKg+Xh2fHswZdv+xSUwwoy7iWGlaasFKUl+UsS1lphl8L0up8s6a&wx_header=3&from=industrynews&color_scheme=light

原始代码链接：https://www.gitpp.com/chatwike/project-gpp-0525002

基于深度学习的低代码计算机视觉系统，包含图像采集、智能检测、数据标注、模型训练四大模块。

## 项目特点

- 实时性：单张检测耗时<2秒
- 准确性：字符识别率≥99.5%
- 追溯性：所有检测记录可存储6个月
- 工业级UI：符合工业软件设计规范
- 设备集成：支持PLC/OPC UA/MES系统对接

## 核心功能

- 实时视频流预览与检测
- 检测结果瀑布流展示
- 质量统计看板
- 历史记录查询与管理
- 标注数据管理与样本库版本控制
- 模型训练与性能监控

## 技术栈

- 前端：Vue 3 + Vite + Quasar
- 可视化：ECharts工业大屏版
- 图像处理：OpenCV
- 深度学习：TensorFlow/PyTorch/ONNX
- 数据存储：IndexedDB
- 设备通信：WebSocket + OPC UA

## 启动方式：分两步 第一步启动服务端server 第二步 npm run dev


1)本地服务器启动
2)本地客户端启动，简单的vite配置 看 vite.config文件; 安装node ； npm run dev自动启动

### 1. 双击 start.bat

![alt text](</README-PHOTOS/20250424051101.png>)

![alt text](</README-PHOTOS/20250424143027.png>)

### 2. 启动前端 进入文件夹 npm run dev 自动弹出浏览器  ---》  点击设置 语言

![alt text](</README-PHOTOS/fc273eca3328921851e2d0ab130b5e4.png>)

### 3. 修改语言

![alt text](</README-PHOTOS/5d038ed7c1369f2d13502c354727de1.png>)

相机等硬件会自动连接，也可在设置中自行添加。

### 4. 数据标注

![alt text](</README-PHOTOS/b9014ec2a523cff7a627f09042641f4.png>)

红框内图片是为了训练模型正确找到文本区域

蓝框内图片是为了训练模型正确识别文本内容

### 5. 合成数据

![alt text](/README-PHOTOS/75c3321edb28ee14457d976652e6bc1.jpg)

### 6. 图像处理

![alt text](</README-PHOTOS/20250424143954.png>)

先设置单步处理，再将单步处理通过串联的方式形成流水线处理

![alt text](</README-PHOTOS/f193d218453a12e65a9970fa06f83dd.png>)

### 7. 模型调用

![alt text](</README-PHOTOS/1f45896e0e349076c2df3fa8cb65858.png>)

复制模型ID

![alt text](</README-PHOTOS/1745480781735.jpg>)

调用模型

### 8. 实时监控

![alt text](</README-PHOTOS/bd2d2785fbf9d294e2bd1fa87d5da99.jpg>)

在实时监控页面可以选择刚才设置的单步处理或流水线处理来对图像进行修改

 
