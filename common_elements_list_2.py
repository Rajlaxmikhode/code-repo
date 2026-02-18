li1=[2,4,6,8,7]
li2=[1,3,5,7,8,2]
li1.sort()
li2.sort()
common_elemets=[]

for i in li1:
    for j in li2:
        if i==j:
          common_elemets.append(i)
print("Thecommon elements in the list:",common_elemets)

    