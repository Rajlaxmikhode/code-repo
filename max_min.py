li=[2,4,1,6,8,9]
max_val=li[0]
min_val=li[0]
for i in range(len(li)):
    if li[i]>max_val:
        max_val=li[i]
    if li[i]<max_val:
        min_val=li[i]
print("maximum value =",max_val)
print("Minimum value =",min_val)
