Missionaries_on_right=3
Cannibals_on_right=3
Missionaries_on_left=0
Cannibals_on_left=0
boat_side="right"
while True:
    print("=====================================")
    print("Right side || Left side")
    print("M:",Missionaries_on_right,"c:",Cannibals_on_right,
                     "  ||   ",
          "M:",Missionaries_on_left,"C:",Cannibals_on_left)
    print("Boat side:",boat_side)
    print("=====================================\n")
    if Missionaries_on_left==3 and  Cannibals_on_left==3:
        print("You solved it hurray!...")
        break

    m=int(input("Enter the missionaries to move"))
    c=int(input("Enter the cannibals to move"))

    if m+c<1 or m+c>2:
        print('Invalid move')
    if boat_side=="right":

        if m>Missionaries_on_right or c>Cannibals_on_right:
            print("Invalid move")
            continue
        print(f"moving missionaries{m} and cannibals {c} from right to left")

        Missionaries_on_right-=m
        Cannibals_on_right-=c
        Missionaries_on_left+=m
        Cannibals_on_left+=c
        boat_side="left"

    else:
        if m>Missionaries_on_left or c>Cannibals_on_left:
            print("Moving from left to right")
            continue
        Missionaries_on_left-=m
        Cannibals_on_left-=c
        Missionaries_on_right+=m
        Cannibals_on_right+=c
        boat_side="right"

        if (Missionaries_on_right>0 and Cannibals_on_right>Missionaries_on_right)or(Missionaries_on_left>0 and Cannibals_on_left>Missionaries_on_left):
            print("Cannibals ate the missionaries")

            break