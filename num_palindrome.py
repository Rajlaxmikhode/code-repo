n=int(input("Enter number: "))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("Given number ia a 'palindrome' ")
else:
    print("given number is not a 'palindrome' ")





