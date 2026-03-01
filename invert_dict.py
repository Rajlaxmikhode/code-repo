#inverted dictionary
dictionary={"a":1,"b":2,"c":3,"d":1}
inverted={}
for key,value in dictionary.items():
    inverted.setdefault(value,[]).append(key)
print(inverted)