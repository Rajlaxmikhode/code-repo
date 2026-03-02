def number_pattern(n):
    if not isinstance(n,int):
        return "Argument must be an integer value"
    if n<1:
        return "Argument must be an integer greater than 0"
    res=''
    for i in range(1, n+1):
      res+=str(i)+' '
    print(res)
    return res.strip
num=input("Enter any number: ")

print(number_pattern(num))
