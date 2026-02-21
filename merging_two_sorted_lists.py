#merge two sorted lists
li1=[1,2,3,2,1]
li2=[4,1,8,6]
sorted_list=sorted(li1+li2)
print(sorted_list)
print()

#DSA-style way to merge two sorted lists
list_1=[11,30,27,74,40,83]
list_2=[9,13,2,70,24,53]
li1.sort()
li2.sort()

i=j=0
merged=[]

while (i<len(list_1)) and (j<len(list_2)):
    if list_1[i]<list_2[j]:
        merged.append(list_1[i])
        i+=1
    else:
        merged.append(list_2[j])
        j+=1
    
#add remaining elements
merged.extend(list_1[i:])
merged.extend(list_2[j:])

print(merged)



