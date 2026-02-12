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





