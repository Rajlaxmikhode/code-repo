def add(a,b):
    res=a+b
    if  res % 2==0:
        print("Sum of given two digits is even")
    else:
        print("Sum of given two digits is odd")
    return res
   
res=add(8,7)
print(res)