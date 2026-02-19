#Rotate list left by k steps
li=[1,2,3,4,5,6,7]
k=3
k=k%len(li)
left_rotate=li[k:]+li[:k]
right_rotate=li[-k:]+li[:-k]
print("Left Rotate:",left_rotate)
print("Right Rotate:",right_rotate)