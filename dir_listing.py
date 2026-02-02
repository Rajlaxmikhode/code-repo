from pathlib import Path
path=Path()
count=0
for item in path.rglob("*"):
    if item.is_dir():
        print("Dir: ",item)
    else:
        print("File: ",item)
        count+=1
print(count)