# 思贤家教 · 商河本地上门辅导

商河本地家教网站。静态页面发布到 GitHub Pages，Flask 后端用于后台管理。

## 项目结构

```
sixian-edu/
├── server/                 # Flask 后端
│   ├── app.py             # 主应用
│   ├── models.py          # 数据库模型
│   ├── config.py          # 配置
│   ├── seed.py            # 数据填充脚本
│   ├── requirements.txt   # Python 依赖
│   ├── Dockerfile
│   ├── .env               # 环境变量
│   ├── templates/         # Jinja2 模板
│   │   ├── index.html     # 首页模板
│   │   ├── teachers.html  # 老师列表
│   │   ├── admin/         # 后台管理模板
│   │   └── ...
│   └── instance/          # SQLite 数据库
├── images/                # 图片资源
│   ├── liulaoshi.jpg
│   ├── dilaoshi.jpg
│   └── ...
├── 老师信息/              # 老师静态详情页
├── index.html             # 根 URL 重定向
├── 思贤家教.html          # 静态主页
├── 老师.html              # 静态老师列表页
├── 算法助学.html          # AI 错题分析
├── 加入思贤.html          # 合作联系
├── 预约试听.html          # 预约试听
├── 思贤公约.html          # 家教公约
├── 真题.html              # 历年真题
├── .claude/
├── .gitignore
├── CLAUDE.md
└── 部署说明.md
```

## 部署

- **静态站**: GitHub Pages（master 分支根目录自动部署）
- **后端**: Flask 应用，本地或 Docker 运行

## 设计规范

- 主色: `#1a1a2e`（深蓝黑）
- 渐变: `linear-gradient(135deg, #1a1a2e, #16213e, #2d3436)`
- 字体: `-apple-system, "Microsoft YaHei", "PingFang SC", sans-serif`
- 圆角: 14-16px（卡片）, 8-10px（按钮/输入框）
- 阴影: `0 2px 16px rgba(0,0,0,0.06)`
- 背景: `#f8f9fc`
- 联系方式: 155-6412-8008（微信同号）

## 合规注意事项（2026-05-15 整改后）

- 品牌名已从"思贤教育"改为"思贤家教"——避免"教育"暗示注册机构
- 所有页面已去除机构化用语（"成立于"、"工作室"、"平台"、"管理费"、"招聘"等）
- 去除"自研AI"等虚假宣传用语
- 去除产品销售（算法助学定价50/70元）
- 去除招聘表单
- 去除平台规则"不接私单"
- Logo 图片（images/logo.jpg 等不合规图片）已删除

## 开发规范

- 中文沟通，回复简洁
- 所有页面保持导航栏一致
- 新增页面同步更新所有导航链接
- 不引入外部依赖（除非必要）
- 移动端优先响应式设计
