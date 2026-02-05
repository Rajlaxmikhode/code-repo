def palindrome_check(st):
    if len(st)==1:
        return True
    if st[0]!=st[-1]:
        return False
    return palindrome_check(st[1:-1])

str=input("Enter a string: ")
print(palindrome_check(str))



