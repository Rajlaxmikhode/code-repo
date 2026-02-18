#Flatten a nested list 
li=[2,4,[5,7,5],5,0,[7,1],9,11]

flat=[]

for item in li:
    if isinstance(item,list):
        for element in item:
            flat.append(element)
    else:
        flat.append(item)
        
print(flat)
    
    