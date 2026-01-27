for i in range(4):
    print("*",end="")
print()
for j in range(2):
    print("*",end="")
print()
for k in range(4):
    print("*",end="")
print()
for l in range(2):
    for k in range(2):
        print("*",end="")

    print()
print("--------------------------------------")
#we can use list for this pattern itt'ss an easy way
rows=[4,2,4,2,2]
for r in rows:
    for x in range(r):
        print("X",end="")
    print()