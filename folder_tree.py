import os
import argparse
import fnmatch

def load_ignore_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines()]
            return [line for line in lines if line and not line.startswith('#')]
    except FileNotFoundError:
        print(f"⚠️  Ignore file not found: {path}")
        return []
    except Exception as e:
        print(f"❌ Error reading ignore file: {e}")
        return []

def matches_exclude(path, exclude_patterns, root_path):
    rel_path = os.path.relpath(path, root_path).replace("\\", "/")
    for pattern in exclude_patterns:
        if fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(os.path.basename(rel_path), pattern):
            return True
    return False

def list_tree(start_path, prefix="", output_lines=None, exclude_patterns=None, root_path=None, show_files=False):
    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        line = f"{prefix}📁 [Permission Denied] {os.path.basename(start_path)}"
        (output_lines.append(line) if output_lines else print(line))
        return

    # Filter folders and files separately
    folders = [e for e in entries if os.path.isdir(os.path.join(start_path, e)) and not matches_exclude(os.path.join(start_path, e), exclude_patterns, root_path)]
    files = [e for e in entries if os.path.isfile(os.path.join(start_path, e))] if show_files else []

    all_entries = folders + files
    total = len(all_entries)

    for idx, entry in enumerate(all_entries):
        path = os.path.join(start_path, entry)
        is_last = (idx == total - 1)
        connector = "└── " if is_last else "├── "
        is_file = os.path.isfile(path)
        icon = "📄" if is_file else "📁"
        line = f"{prefix}{connector}{icon} {entry}"
        (output_lines.append(line) if output_lines else print(line))

        if not is_file:
            new_prefix = prefix + ("    " if is_last else "│   ")
            list_tree(path, new_prefix, output_lines, exclude_patterns, root_path, show_files)

def main():
    parser = argparse.ArgumentParser(description="Folder Tree Viewer with exclusions and file support")
    parser.add_argument('--origin', type=str, help='Starting directory (default: current working directory)')
    parser.add_argument('-o', action='store_true', help='Save output to "folder_tree.txt" in current directory')
    parser.add_argument('--output', type=str, help='Save output to a specific file path')
    parser.add_argument('--exclude', nargs='*', default=[], help='Exclude folders/files (.gitignore-style patterns)')
    parser.add_argument('--folderignore', type=str, help='Path to ignore file (e.g. .ignore)')
    parser.add_argument('--all-files', '-f', action='store_true', help='Include files in the tree output')

    args = parser.parse_args()

    if args.output and args.o:
        print("❌ Error: Use either `-o` or `--output <path>`, not both.")
        return

    origin = os.path.abspath(args.origin if args.origin else os.getcwd())
    origin_display_name = os.path.basename(origin.rstrip(os.sep)) or origin
    output_lines = [f"📁 {origin_display_name}"]

    exclude_patterns = args.exclude or []
    if args.folderignore:
        exclude_patterns += load_ignore_file(args.folderignore)

    list_tree(origin, output_lines=output_lines, exclude_patterns=exclude_patterns, root_path=origin, show_files=args.all_files)

    if args.output:
        output_path = args.output
    elif args.o:
        output_path = os.path.join(os.getcwd(), "folder_tree.txt")
    else:
        print("\n".join(output_lines))
        return

    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(output_lines))
        print(f"✅ Tree saved to: {output_path}")
    except Exception as e:
        print(f"❌ Failed to write output: {e}")

if __name__ == "__main__":
    main()
