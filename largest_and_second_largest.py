num=[100, 209, -3789, 4000, 500, 10]
max=num[0]
sec_max = float('-inf')

for i in num:
    if i>max:
        max=i

for j in num:
    if j<max and j>sec_max:
        sec_max=j
print("Largest= ",max)        
print("second Largest= ",sec_max)