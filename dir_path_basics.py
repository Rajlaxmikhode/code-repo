from pathlib import Path
path=Path()
for file  in path.glob("*.py"):#searches .py files in ccurrent dir
    print(file)
print()
for files in path.glob('*'): #It shows what the directory contains non recursive means  doesn't go inside the subfolder
    print(files)
print()
for files in path.rglob("*"): #recursive goes inside all files
    print(files)


