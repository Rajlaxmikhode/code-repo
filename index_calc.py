#numbers = list(map(int, input().split()))

#if 8 in numbers:
 #   print(numbers.index(8))


numbers = list(map(int, input().split()))
val=False
for index, value in enumerate(numbers):
    if value==8:
       val=True
       break
if val==True:       
    print(index)