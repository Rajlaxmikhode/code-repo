#Check for armstrong number:
n=int(input("Enter a number: "))
temp=n
sum=0
r1=len(str(n))
while n>0:
    r=n%10
    sum=sum+r**r1
    n=n//10
if temp==sum:
    print("Given number is a armstrong number")
else:
    print("The given number is not a armstrong number")
