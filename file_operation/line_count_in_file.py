line_count=0
word_count=0
with open("hello.txt","r") as file:
    for line in file:
        line_count+=1
        word_count+=len(line.split())
print("Number of line in the file",line_count)
print("Number of word in the file:",word_count)