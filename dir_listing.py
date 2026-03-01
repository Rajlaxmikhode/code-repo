from pathlib import Path
path=Path()
count=0
for item in path.rglob("*"):
    if item.is_dir():#If it's a folder → print "Dir:"
        print("Dir: ",item)
    else:
        print("File: ",item)
        count+=1
print(count)
