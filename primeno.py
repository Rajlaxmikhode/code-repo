n=int(input("Enter"))
prime=n
if (n>1):
    for i in range(1,11):

        if (n%1==0) and (n%i!=0) and (n%n==0):
           
           print("Is prime",prime)               

        else:
            print("Is not prime",prime)  
        

             
        
