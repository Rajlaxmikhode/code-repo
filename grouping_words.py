#grouping words based on length of the word
words=["mango","cherry","banana","apple","orange"]
grouped={}
for word in words:
    length=len(word)
    grouped.setdefault(length,[]).append(word)
print(grouped)


