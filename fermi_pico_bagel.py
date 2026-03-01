import random
num=random.randint(100,999)
original_number=str(num)
attempts=0
max_attempts=8
while attempts<max_attempts:
    clues=[]
    guess_number=str(input("Guess the number: "))

    if len(original_number)!=len(guess_number):
        print(f"Enter {len(original_number)} digits")
        continue
    
    if len(set(guess_number))!=3:#set don't consider the duplicate element
        print("Unique elements only")
        continue

    attempts+=1

    if guess_number==original_number:
        print("Congratulations🎉!You guessed it right")
        print("Attempts: ",attempts)
        break


    for i in range(3):
        if guess_number[i]==original_number[i]:
            clues.append("fermi")
        if guess_number[i]!=original_number[i] and guess_number[i] in original_number:
            clues.append("pico")


    if clues==[]:
        print("bagel")
    else:
        print(" ".join(clues))

    print("Attempts  left= ",max_attempts-attempts)

else:
    print("--Game over--")
    print("Original number: ",original_number)

