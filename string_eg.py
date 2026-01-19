string="hello"
#vowels='aeiou'
count=0
for x in range(len(string)):
    if string[x] in 'aeiou':
        count+=1
    
print(count)
