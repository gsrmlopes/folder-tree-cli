# 📁 Folder Tree CLI Tool

A lightweight Python command-line tool to display or export a folder tree structure, with support for:

- ✅ Recursive directory traversal
- 📄 Optional file listing
- 🚫 `.gitignore`-style exclusions
- 📂 Ignore list via `.ignore`-style file
- 💾 Export to a `.txt` file

---

## 📦 Installation

> Requires **Python 3.6+**

Clone or download this repo:

```bash
git clone https://github.com/gsrmlopes/folder-tree-cli.git
cd folder-tree-cli
```

Make the script executable on linux:

```bash
chmod +x folder_tree.py
```

Or just run it with Python:

```bash
python folder_tree.py
```

---

## 🚀 Usage

```bash
python folder_tree.py [options]
```

### 🔧 Options

| Flag                      | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `--origin <path>`         | Start tree from this folder (default: current working directory)            |
| `-f`, `--all-files`       | Include files in the tree output                                            |
| `--exclude <patterns>`    | Exclude folders/files by pattern (supports `.gitignore` syntax)             |
| `--folderignore <file>`   | Read exclusion patterns from a file (e.g. `.ignore`, `my-ignore.txt`, etc.) |
| `-o`                      | Save output to `folder_tree.txt` in the current directory                   |
| `--output <path>`         | Save output to a custom file path                                           |

> ⚠️ Do not use `-o` and `--output` together.

---

## 🧪 Examples

### Print just the folder structure:
```bash
python folder_tree.py
```

### Print including files:
```bash
python folder_tree.py -f
```

### Save to a file:
```bash
python folder_tree.py -o
```

### Use a custom ignore file:
```bash
python folder_tree.py --folderignore .ignore
```

### Exclude with patterns (like `.gitignore`):
```bash
python folder_tree.py --exclude '__pycache__' '.git' '*.egg-info'
```

### Combine everything:
```bash
python folder_tree.py --origin ./project --exclude node_modules dist --folderignore .ignore -f --output project_tree.txt
```

---

## 📝 .ignore File Format

Use `.gitignore`-style patterns to exclude folders:

```
# Ignore folders
node_modules
dist
__pycache__

# Wildcards supported
*.egg-info
.*           # hidden folders
src/**/temp  # nested
```

---

## 📄 License

MIT License © 2025 [gsrmlopes]
