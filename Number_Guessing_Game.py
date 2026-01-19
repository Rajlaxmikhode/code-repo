import random

number_to_guess=random.randint(1,100)

while True:
    try:
        guess=int(input("Guess the number: "))

        if guess>number_to_guess:
            print("too high")
        elif guess<number_to_guess:
            
            print("too low")
        else:
            print('you gussed it right')
            break
    except ValueError:
        print("enter a valid value")