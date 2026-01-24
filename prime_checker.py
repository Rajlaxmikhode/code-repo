def prime(num):
    if num<2:
        print("The given number is not a prime number")
        return 
    for i in range(2,num):
        if num%i==0:
            print("The given number is not a  prime number")
            return 
    print("the given number is a prime number")
print(prime(9))
        


            

