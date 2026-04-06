from pathlib import Path

path = Path(r"C:\Users\Laptronics\Desktop\Git p")  # change this to your folder path

count = 0

for file in path.rglob("*.py"):
    count += 1

print("Total .py files:", count)