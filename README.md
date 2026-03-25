# 知识管理工具 (Knowledge Manager Tool)

<p align="center">
  <strong>轻量级知识管理工具，支持自定义分类和标签</strong>
</p>

<p align="center">
  <a href="https://liutg.github.io/knowledge-manager-tool/" target="_blank">
    <img src="https://img.shields.io/badge/官网-点击访问-blue?style=for-the-badge" alt="官网">
  </a>
  <a href="https://github.com/LiuTG/knowledge-manager-tool" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-仓库地址-black?style=for-the-badge&logo=github" alt="GitHub">
  </a>
  <a href="https://gitee.com/liusanye/knowledge-manager-tool" target="_blank">
    <img src="https://img.shields.io/badge/Gitee-仓库地址-red?style=for-the-badge" alt="Gitee">
  </a>
</p>

<p align="center">
  <a href="#功能特性">功能特性</a> •
  <a href="#安装使用">安装使用</a> •
  <a href="#使用指南">使用指南</a> •
  <a href="#技术栈">技术栈</a> •
  <a href="#关于作者">关于作者</a>
</p>

> **项目官网**: https://liutg.github.io/knowledge-manager-tool/  
> 点击上方链接即可访问项目官网，了解软件详细介绍和使用说明。

---

## 项目简介

知识管理工具是一款基于 PyQt5 开发的桌面应用程序，旨在帮助用户高效管理各类知识资源。通过自定义分类、标签系统和强大的搜索功能，让您轻松组织和检索知识内容。

**作者**：《下班两小时》频道 B站UP主：下班的三爷

## 功能特性

### 核心功能

#### 项目管理
- 创建、编辑、删除知识项目
- 支持自定义项目类型和配置
- 项目数据本地存储，安全可靠
- 支持项目导入导出

#### 资源管理
- 多类型资源支持（链接、文件、笔记等）
- 资源分类与标签系统
- 资源快速检索与过滤
- 批量添加资源功能

#### 提示词管理
- 提示词分类存储
- 快速复制功能
- 提示词与资源绑定
- 场景化提示词管理

#### 笔记功能
- Markdown 格式支持
- 笔记与资源关联
- 笔记编辑与预览

### 界面特性

- 现代扁平化设计风格
- 统一的设计系统（颜色、圆角、间距、字体）
- 响应式窗口布局
- 适配多种屏幕分辨率
- 支持深色/浅色主题

### 数据管理

- JSON 格式本地存储
- 数据自动备份
- 支持数据导入导出
- 项目数据隔离

## 安装使用

### 环境要求

- Python 3.8+
- PyQt5

### 安装依赖

```bash
pip install PyQt5
```

### 运行程序

```bash
python knowledge_manager_tool.py
```

### 打包发布

使用 PyInstaller 打包为独立应用：

```bash
pyinstaller --onefile --windowed knowledge_manager_tool.py
```

## 使用指南

### 快速开始

1. **创建项目** - 首次使用时，点击"新建项目"创建您的知识库
2. **添加资源** - 在项目中添加各类知识资源（链接、文件、笔记等）
3. **分类管理** - 使用分类和标签组织您的资源
4. **快速检索** - 使用搜索功能快速定位所需内容

### 项目类型

支持多种项目类型配置：
- 默认项目
- 自定义项目类型
- 可扩展的项目模板

### 资源类型

| 类型 | 说明 |
|------|------|
| 链接 | 网页链接资源 |
| 文件 | 本地文件资源 |
| 笔记 | 文本笔记内容 |
| 提示词 | AI 提示词模板 |

### 快捷操作

- 双击资源卡片查看详情
- 右键菜单快速操作
- 快捷键支持常用功能

## 技术栈

- **GUI 框架**: PyQt5
- **数据存储**: JSON
- **设计模式**: MVC 架构
- **UI 风格**: 现代扁平化设计

### 核心模块

| 模块 | 说明 |
|------|------|
| DesignSystem | 统一设计系统，管理颜色、字体、间距等 |
| KnowledgeManagerTool | 主窗口，应用入口 |
| ProjectDialog | 项目管理对话框 |
| ResourceInventoryDialog | 资源清单管理 |
| NoteEditDialog | 笔记编辑对话框 |
| PromptListItemWidget | 提示词列表项组件 |

## 目录结构

```
knowledge-manager-tool/
├── knowledge_manager_tool.py  # 主程序文件
├── README.md                  # 项目说明
├── index.html                 # 项目官网
└── LICENSE                    # 开源协议
```

## 数据存储

项目数据存储在用户目录下：

```
~/.knowledge_manager/
├── projects/           # 项目数据
│   ├── project_1.json
│   └── project_2.json
├── resources/          # 资源数据
└── config.json         # 配置文件
```

## 开发计划

- [ ] 支持云端同步
- [ ] 支持团队协作
- [ ] 支持插件扩展
- [ ] 支持更多资源类型
- [ ] 移动端适配

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交 Pull Request

## 开源协议

本项目采用 MIT 协议开源，详见 [LICENSE](LICENSE) 文件。

## 关于作者

**下班的三爷**

- B站频道：《下班两小时》
- 专注于效率工具开发和知识管理方法论分享

---

<p align="center">
  如果这个项目对您有帮助，请给一个 ⭐️ Star 支持一下！
</p>
