li=[2,6,3,2,4,5,2]
li.sort()
print("Sorted list:",li)
new_li=[]
for i in li:
    if i not in new_li:
        new_li.append(i)        
print(new_li)
