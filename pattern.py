#Pattern 
print("printing stars in in creeasing order")
print()
rows=5
for i in range(rows):
    for j in range(i+1):
        print("*",end=" ")
    print()

print("-------------------------------------")
print()

print("printing stars in decreasing order")
print()
rows=5
for i in range(rows):
    for j in range(i,rows):
        print("*",end=" ")
    print()

print("-------------------------------------")
print()

#printing numbers for 1-5 inn right angled form
print("Number pattern in increasing order")
print()

rows=5
for i in  range(1,rows+1):
    for j in range(i):
        
        print(j+1,end=' ')
    print()

print("-------------------------------------")
print()

print("printing stars in decreasing order")
print()

rows=5
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
print("-------------------------------------")
print()

#printing numbers in a triangle format
print("pyramid")
print()

for i in range(1,6):
    print(" "*(5-i),end='')
    for j in range(1,i+1):
        print(j,end=' ')
    print()
print("-------------------------------------")
print()

print("tringle in right sided")
print()
for i in range(1,6):
    for j in range(i,6):
        print(" ",end=" ")
    for j in range(i):
        print('*',end=' ')
    print()

print("-------------------------------------")
print()

print("tringle in decreasinng order in left side")
print()
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,5):
        print("*",end=" ")
    print()
print("-------------------------------------")
print()

print("hill pattern")
print()
for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
        
    print()
print("-------------------------------------")
print()


print("reverse hill pattern")
print()
for i in range(5):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,5):
        print("*",end=" ")
    for j in range(i,4):
        print("*",end=" ")
    print()

print("-------------------------------------")
print()


print("diamond shape ")
print()
for i in range(5):
    for j in range(i,5):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for k in range(5):
    for l in range(k+1):
        print(" ",end=" ")
    for l in range(k,5):
        print("*",end=" ")
    for l in range(k,4):
        print("*",end=" ")
    print()




