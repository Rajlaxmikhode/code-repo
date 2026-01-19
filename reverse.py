num=234
temp=num
rev=0
while  num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("Reverse of given number is",rev)