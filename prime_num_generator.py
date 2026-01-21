#program to generate prime numbers  upto n
n=int(input("Enter a number: "))
print(f"prime numbers till {n} are:")
if n>0:
    for i in range(2,n+1):
        is_prime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:

                is_prime=False
                break
        if is_prime:
            print(i)

