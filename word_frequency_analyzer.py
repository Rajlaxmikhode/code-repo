# word frequency analyzer
text=input("Enter a string:").lower()
freq={}
for word in text.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("\nfrequencies is:")
for word,count in freq.items():
    print(f"{word}:{count}")     
check_word=input("Enter a word to check it's frequency:  ").lower()
print(f"{check_word} appeared {freq.get(check_word),0} times.")