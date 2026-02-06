#experimental based check on prime number property 
# Works for all primes > 3, but may return True for some non-primes 


def fun(num):

    if num<1:
        print("The given number is not a prime number")
        return False
    elif num<=3:
        #print("The given number is a prime number")
        return True
    elif ((num**2)-1)%24==0:
        #print("The given number is a prime number")
        return True
    else:
        #print("The given number is not a prime number")
        return False
    
        
   
number=int(input("Enter a  number: "))
print(fun(number))
