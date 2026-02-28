def fun(n):
    '''This function takes the  integer n as input and returns the cube of it.'''
    return n**3

num=int(input("Enter a number:"))
print(fun(num))
print(fun.__doc__) #This will print docstring of the function fun.