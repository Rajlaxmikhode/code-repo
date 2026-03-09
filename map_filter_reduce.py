#MAP
def fun(x):
    return x*x*x

print(fun(9))
#using map
tup_1=(2,4,2,5,6,9)
new=tuple(map(fun,tup_1))
print(new)

#FILTER
def filter_fun(y):
    return y%2==0

new_tup=tuple(filter(filter_fun,tup_1))
print(new_tup)

#REDUCE
from functools import reduce

# def fx(m,n):
#     return m+n

red=reduce(lambda m,n: m+n,tup_1)
print(red)