with open("hello.txt","r") as f:
    lines=f.readlines()
    for line in lines:
       print(line)