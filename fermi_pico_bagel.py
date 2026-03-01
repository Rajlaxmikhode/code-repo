import random
num=random.randint(100,999)
original_number=str(num)
while True:
    clues=[]
    guess_number=str(input("Guess the number: "))
    if len(original_number)!=len(guess_number):
        print(f"Enter {len(original_number)}")
        break
    
    if guess_number==original_number:
        print("Congratulations🎉!You guessed it right")
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


