def fun(st):
    rev=""
    for i in st:
        rev=i+rev
    return rev
print(fun("hello"))