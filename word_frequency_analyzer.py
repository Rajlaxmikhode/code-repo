# word frequency analyzer
import re
text=input("Enter a string:").lower()

text = re.sub(r'[^\w\s]', '', text)
freq={}
for word in text.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
print("\nfrequencies is:")
for word,count in freq.items():
    print(f"{word}:{count}")   

check_word=input("\nEnter a word to check it's frequency: ").lower()
print(f"'{check_word}' appeared {freq.get(check_word),0} times.")