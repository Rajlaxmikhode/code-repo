distance_mi=2
is_raining=True
has_bike=True
has_ride_share_app=True
has_car=True

if distance_mi<=1:
    if not is_raining:
        print(True)
    else:
        print(False)

elif 1< distance_mi <=6:
    if has_bike and not is_raining==True:
        print(True)   
    else:
        print(False)

else :
    if has_car  or  has_ride_share_app:
        print(True)
    else:
        print(False) 


# by using function we can minimize the number of lines of the code
def travel_planner(distance_mi,is_raining,has_car,has_bike,has_ride_share_app,):
    #short distance:If a person can walk
    if distance_mi<=1:
        return not is_raining
    #for long distance :by bike or car
    elif 1< distance_mi <=6:
        return has_bike and is_raining
    else:
        return has_ride_share_app or has_car
    

res=travel_planner(7,True,False,True,True)
print("Calculation using function:",res)



