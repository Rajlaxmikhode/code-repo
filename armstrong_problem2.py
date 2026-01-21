for i in range(1,1000):
    temp=i
    st=str(i)
    l=len(st)
    num=0
    while i>0:
        r=i%10
        
        num += r ** l
        i=i//10
    if temp==num:
        print(temp)
else:
        print("bye")
    

