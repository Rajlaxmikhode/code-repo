def count(phrase):
    return len(phrase.split())
print(count("hey hhi this is me"))
print("________________________________________\n")
def word(phrase):
    count=0
    for w in phrase.split():
        count+=1
    return count
print(word("hey she is myra right haa"))

