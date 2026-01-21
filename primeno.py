n=int(input("Enter"))

if (n>1):
    is_prime=True
    for i in range(2,n):
        if n%i==0:

            is_prime=False
            break
    if is_prime:
        print("The given number is a prime number")
    else:
        print(n,"Not a prime number")
else:
    print(n,"Not a prime number")


        
             
        
