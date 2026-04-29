#Zip function
first_name=['Riya','Anu','Vinayak','Rohit']
last_name=['Pawar','Kalaburgi','Khode','Roy']
for f, l in zip(first_name,last_name):
    print(f, l)


#Map Function
li=[2,3,'sea','cloud',5.90,6,7]
res=tuple(map(lambda x: (x,type(x)),li))
print(res)

#Filter Function
is_even=lambda x: x%2==0
res=list(filter(is_even,range(1,21)))
print(res)