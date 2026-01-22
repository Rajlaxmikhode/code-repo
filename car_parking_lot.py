max_capacity=10
min_capacity=0
no_cars=0

while True:
    
    if max_capacity==min_capacity:
        print("Parking lot is full 🫷")
        break
    print("parking space for cars available is: ",max_capacity)

    try:
        car_entry=int(input("If car enters one or if exits zero: "))
    except ValueError:
        print("Enter a valid value")
    
    if car_entry!=0 and car_entry!=1:
        print("❌ Invalid move")
        continue

    if car_entry==1:
        no_cars+=1
        max_capacity-=1

    else:
        if no_cars>0:
            no_cars-=1
            if max_capacity<10:
                max_capacity+=1
        else:
            print("no cars to exit 🚪")
    if no_cars!=0:
        print("No of cars🚘  in parking lot:\n ",no_cars)
      

    



