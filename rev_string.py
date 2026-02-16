def fun(string):
    rev=""
    for i in string:
     rev=i+rev
    return rev
print(fun("hello"))