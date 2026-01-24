def fun(st):
    vowels="aeiou"
    count=0
    for ch in st:
        if ch.lower() in st:
            count+=1
    return count
    
print(fun("aeiou"))