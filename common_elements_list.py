li1=[2,4,6,8,7]
li2=[1,3,5,7]
li1.sort()
li2.sort()

found=False
for i in li1:
    for j in li2:
        if i==j:
           
            found=True
            break
    if found:
        break
if found:
    print("There is  a common element in the list:",i)
else:
    print("no common element")
    