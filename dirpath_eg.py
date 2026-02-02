#Working with dirictories 
from pathlib import Path
path=Path("main.py")
print(path.exists())
path1=Path("main3.py")
print(path1.mkdir()) #This creates a  Directory named "main3.py"
#print(path1.rmdir()) This removes a dir_path (must bbe empty)


