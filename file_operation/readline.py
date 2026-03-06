#this will read only one line
with open("hello.txt","r") as f:
   print(f.readline())

# Using while loop we can read all lines
print("Using for loop")
with open("hello.txt","r") as f:
   while True:
    line=f.readline()
    if not line:
        break
    print(line)
