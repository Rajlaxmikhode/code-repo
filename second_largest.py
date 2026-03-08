li=[10,20,4,45,99]
max1=max2=float('-inf')
for num in li:
    if num>max1:
       max2=max1
       max1=num       
    elif num>max2 and num!=max1:
        max2=num
print(max2)

    