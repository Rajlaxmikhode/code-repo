longest_word=""
with open("hello.txt","r") as file:
    for line in file:
        words=line.split()
        for word in words:
            if len(longest_word)<len(word):
                longest_word=word
print("Longest word:",longest_word)

            