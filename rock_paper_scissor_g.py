import random
emojis={"rock": "🪨", "paper": "📃", "scissor": "✂️"}
choices=["rock","paper","scissor"]
player_p=0
computer_p=0
while True:
    player=input(("Enter your choice or(q to quit): "))
    if player=="q":
        print("Thanks for playing!")
        print("player points= ",player_p)
        print("computer points= ",computer_p)
        break
    if player not in choices:
        print("Invalid choice!")
        continue
    computer=random.choice(choices)
    print(f"player choise= {emojis[player]}")
    print(f"computer choice= {emojis[computer]}")
    if ( player=="rock" and  computer=="scissor") or (player=="paper" and computer=="rock") or (player=="scissor" and computer=="paper"):
        player_p+=1
        print("\n you won 🫵")
    else:
        computer_p+=1
        print("computer won 🖥️")
