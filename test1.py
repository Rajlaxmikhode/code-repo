#Write a program that prints all even numbers between 1 and 20 except numbers divisible by 4.

for  i in range(21):
    if i%2==0:
        if i%4==0:
            continue
        else:
            print(i)

    
        