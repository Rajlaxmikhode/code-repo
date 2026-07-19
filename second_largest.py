li= [1, 16, 70, 90, 90, 4, 70, 70]
max1=max2=float('-inf')
for num in li:
    if num>max1:
       max2=max1
       max1=num       
    elif num>max2 and num!=max1:
        max2=num
print("Second_largest = ",max2)

    