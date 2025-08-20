# Our Social Club - 重构版本

一个基于Python和ttkbootstrap的社交俱乐部应用程序，经过完整重构以提供更好的代码组织和可维护性。

## 项目结构

```
Our_Social_Club/
├── src/                    # 源代码目录
│   ├── models/            # 数据模型
│   │   ├── __init__.py
│   │   └── user.py        # 用户模型
│   ├── views/             # 视图层
│   │   ├── __init__.py
│   │   ├── login_window.py    # 登录窗口
│   │   ├── signup_window.py   # 注册窗口
│   │   └── main_window.py     # 主窗口
│   ├── controllers/       # 控制器层
│   │   ├── __init__.py
│   │   └── auth_controller.py # 认证控制器
│   ├── services/          # 业务逻辑层
│   │   ├── __init__.py
│   │   └── user_service.py    # 用户服务
│   ├── components/        # 可复用组件
│   │   ├── __init__.py
│   │   └── blackboard.py      # 公告板组件
│   ├── utils/             # 工具函数
│   │   ├── __init__.py
│   │   └── window_utils.py    # 窗口工具
│   └── config.py          # 配置文件
├── assets/                # 资源文件
│   ├── Background.jpg
│   ├── Main_GUI_Background.png
│   └── Smile.jpg
├── data/                  # 数据文件目录
│   ├── User_file.csv      # 用户登录信息
│   ├── User_info.csv      # 用户详细信息
│   └── blackboard_messages.csv # 公告板消息
├── main.py               # 主程序入口
├── requirements.txt      # 项目依赖
└── README_NEW.md         # 项目说明文档
```

## 架构设计

### MVC架构模式

项目采用MVC（Model-View-Controller）架构模式：

- **Model (models/)**: 数据模型，定义用户类等数据结构
- **View (views/)**: 视图层，负责用户界面的显示
- **Controller (controllers/)**: 控制器层，处理用户输入和业务逻辑

### 关键特性

1. **模块化设计**: 代码按功能分类组织，便于维护
2. **配置集中管理**: 所有配置项统一在`config.py`中管理
3. **服务层分离**: 业务逻辑独立在services层
4. **组件化**: 可复用的UI组件独立封装
5. **类型提示**: 使用Python类型提示提高代码质量

## 安装和运行

### 环境要求

- Python 3.8+
- Windows 10+ (推荐)

### 安装步骤

1. 克隆或下载项目到本地
```bash
git clone <repository-url>
cd Our_Social_Club
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 运行应用
```bash
python main.py
```

## 功能特性

### 已实现功能

- ✅ 用户登录/注册
- ✅ 用户认证系统
- ✅ 学生公告板
- ✅ 基础UI界面

### 计划功能

- 🔲 个人资料管理
- 🔲 好友系统
- 🔲 文件共享
- 🔲 失物招领
- 🔲 意见箱
- 🔲 招聘信息
- 🔲 任务公告板
- 🔲 密保问题
- 🔲 个性化设置

## 技术栈

- **GUI框架**: ttkbootstrap (基于tkinter)
- **图像处理**: Pillow
- **数据存储**: CSV文件
- **密码加密**: SHA256哈希
- **唯一标识**: UUID

## 代码规范

- 使用Python类型提示
- 遵循PEP 8代码风格
- 中文注释和文档字符串
- 错误处理和异常捕获

## 开发指南

### 添加新功能

1. 在相应的层级创建新文件
2. 遵循现有的代码结构和命名规范
3. 更新配置文件（如需要）
4. 添加适当的错误处理

### 文件命名规范

- 使用小写字母和下划线
- 文件名应该清楚地表达其功能
- 视图文件以`_window.py`结尾
- 服务文件以`_service.py`结尾

## 更新历史

### v2.0.0 (2025-08-20) - 重构版本
- 🔄 完全重构代码架构
- ✨ 采用MVC模式
- 🏗️ 模块化设计
- 📝 改进文档和注释
- 🐛 修复原有架构问题

### v1.0 (2024-01-12) - 原始版本
- 基础功能实现
- 单文件架构
- 各种功能模块

## 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

本项目为学习项目，仅供教育使用。

## 联系信息

如有问题或建议，请联系项目维护者。
