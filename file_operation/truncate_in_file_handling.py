with open("text.txt","w") as file:
    data=file.write("This is maya")
    print(file.truncate(7))
    
with open("text.txt","r")as f:
    print(f.read())
