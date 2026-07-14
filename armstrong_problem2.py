for i in range(1,1000):
    temp=i
    st=str(i)
    l=len(st)
    sum=0
    while i>0:
        r=i%10  
        sum += r ** l
        i=i//10
    if temp==sum:
        print(temp)