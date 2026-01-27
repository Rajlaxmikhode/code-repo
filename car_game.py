start=False

while True:
    user=input("Enter: ").lower()
    if user=="help":
        print(''' 
start-To start the car
stop-To stop the car
quit-To quit the game
              ''')
    elif user=="start":
        if start:
            print("car is already started")
        else:
            start=True
            print("car started.......")        
    elif user =="stop":
        if not start:
            print("car is already stopped ")
        else:
            start=False
            print("Car has stopped!")
    elif user =="quit":
        break
    else:
        print("I don't understand")