# 📁 Ferramenta de Linha de Comando para Árvore de Pastas

Uma ferramenta simples em Python para exibir ou exportar a estrutura de diretórios em formato de árvore, com suporte para:

- ✅ Navegação recursiva em diretórios
- 📄 Listagem opcional de arquivos
- 🚫 Exclusões no estilo `.gitignore`
- 📂 Lista de exclusões via arquivo `.ignore`
- 💾 Exportação para arquivo `.txt`

---

## 📦 Instalação

> Requer **Python 3.6+**

Clone ou baixe este repositório:

```bash
git clone https://github.com/gsrmlopes/folder-tree-cli.git
cd folder-tree-cli
```

Torne o script executável (se usando linux):

```bash
chmod +x folder_tree.py
```

Ou execute diretamente com Python:

```bash
python folder_tree.py
```

---

## 🚀 Uso

```bash
python folder_tree.py [opções]
```

### 🔧 Opções

| Flag                      | Descrição                                                                    |
|---------------------------|-------------------------------------------------------------------------------|
| `--origin <caminho>`      | Pasta inicial (padrão: diretório atual)                                      |
| `-f`, `--all-files`       | Inclui arquivos na visualização                                              |
| `--exclude <padrões>`     | Exclui pastas/arquivos (suporta padrões estilo `.gitignore`)                 |
| `--folderignore <arquivo>`| Lê padrões de exclusão de um arquivo (ex.: `.ignore`, `ignorar.txt`, etc.)   |
| `-o`                      | Salva saída em `folder_tree.txt` no diretório atual                          |
| `--output <caminho>`      | Salva a saída em um caminho de arquivo personalizado                         |

> ⚠️ Não use `-o` e `--output` ao mesmo tempo.

---

## 🧪 Exemplos

### Exibir apenas estrutura de pastas:
```bash
python folder_tree.py
```

### Incluir arquivos:
```bash
python folder_tree.py -f
```

### Salvar em arquivo padrão:
```bash
python folder_tree.py -o
```

### Usar arquivo de exclusões personalizado(estrutura .gitignore):
```bash
python folder_tree.py --folderignore .ignore
```

### Excluir por nomeclatura:
```bash
python folder_tree.py --exclude '__pycache__' '.git' '*.conf'
```

### Combinar tudo:
```bash
python folder_tree.py --origin ./projeto --exclude node_modules dist --folderignore .ignore -f --output arvore.txt
```

---

## 📝 Formato do Arquivo .ignore

Use padrões estilo `.gitignore` para excluir pastas/arquivos:

```
# Ignorar pastas
node_modules
dist
__pycache__

# Suporte a curingas
*.egg-info
.*           # pastas ocultas
src/**/temp  # aninhadas
```

---

## 📄 Licença

Licença MIT © 2025 [gsrmlopes]
