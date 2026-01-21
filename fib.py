n=7
a=0
b=1
for i in range(n):
    c=a+b
    temp=a
    a=b
    b=c
    print(temp)