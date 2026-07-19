message=input("Enter you message: ")
words=message.split(" ")
print(words)
emoji={
    ":)":"😀",
    ":(":"😔",
    "<>":"🥱"}
output=""
for word in words:
    output+=emoji.get(word,word) + " " 
    '''
    If word exists in the dictionary → return emoji
    If not → return the word itself
    '''
print(output)

