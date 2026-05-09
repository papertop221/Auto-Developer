import os
import sys

def compress_file(file_path):
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        
        compressed = []
        for line in lines:
            stripped = line.strip()
            # Only keep structural elements (imports, functions, classes)
            if stripped.startswith(("import ", "from ", "def ", "class ", "export ", "const ", "function ")):
                compressed.append(line)
        return "".join(compressed)
    except:
        return ""

def main():
    root_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    summary = []
    
    for root, dirs, files in os.walk(root_dir):
        # Ignore common noise
        if any(x in root for x in [".git", "node_modules", "__pycache__", "dist"]):
            continue
            
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".tsx", ".go", ".rs")):
                full_path = os.path.join(root, file)
                struct = compress_file(full_path)
                if struct:
                    summary.append(f"--- FILE: {full_path} ---\n{struct}")
    
    print("\n".join(summary))

if __name__ == "__main__":
    main()
