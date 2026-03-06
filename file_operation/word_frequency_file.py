freq={}

with open(r"C:\Users\Laptronics\Desktop\Git p\file_operation\hello.txt","r") as file:
    for line in file:
        for word in line.split():
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
for word,count in freq.items():
    print(f"{word}:{count}")





