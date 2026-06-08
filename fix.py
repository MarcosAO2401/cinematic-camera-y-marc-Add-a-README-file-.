import os, re

def fix_file(path):
    with open(path, 'r') as f:
        content = f.read()
    fixed = content.replace('\\n', '\n')
    with open(path, 'w') as f:
        f.write(fixed)
    print(f"Fixed: {path}")

for root, dirs, files in os.walk('app/src'):
    for file in files:
        if file.endswith('.kt') or file.endswith('.java'):
            fix_file(os.path.join(root, file))
print("Done!")
