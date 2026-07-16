import os

directory_paths='C:/Users/Laptronics/Desktop/Git p'
contents=os.listdir(directory_paths)
count=0
for item in contents:
    print(item)
    count+=1
print("Total files: ",count)