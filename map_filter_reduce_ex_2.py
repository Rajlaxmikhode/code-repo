# 1️ Square numbers using map()
# 2️ Keep only numbers > 20 using filter()
# 3️ Add them using reduce()

#1
li = [4, 3, 5, 6, 7, 8, 9, 10, 12, 4]

def square(a):
    return a ** 2
new_list = list(map(square,li))
print(new_list)

#2
def filter_fun(x):
    return x > 20

new = list(filter(filter_fun, new_list))
print(new)

#3
from functools import reduce
add = reduce(lambda m, n: m + n, new)
print(add)

