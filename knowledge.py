from pathlib import Path

# 项目名称
project_name = "MyKnowledge"

# 需要创建的目录
folders = [
    "docs",
    "docs/stylesheets",
    "docs/math",
    "docs/physics",
    "docs/chemistry",
    "docs/python",
    "docs/ai",
    ".github/workflows"
]

# 需要创建的文件
files = {
    "requirements.txt": "",
    "mkdocs.yml": "",
    "docs/index.md": "# 欢迎来到我的知识库\n",
    "docs/about.md": "# 关于我\n",
    "docs/stylesheets/extra.css": "",
    "docs/math/calculus.md": "# 微积分\n",
    "docs/physics/relativity.md": "# 狭义相对论\n",
    "docs/chemistry/basic.md": "# 化工原理\n",
    "docs/python/python.md": "# Python\n",
    "docs/ai/dl.md": "# 深度学习\n",
    ".github/workflows/deploy.yml": ""
}

root = Path(project_name)

# 创建目录
for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

# 创建文件
for filename, content in files.items():
    path = root / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

print(f"项目 {project_name} 创建完成！")