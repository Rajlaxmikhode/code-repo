st="aappyyhe"
count={}
for ch in st:
    count[ch]=count.get(ch,0)+1
for ch in st:
    if  count[ch]==1:
        
       print("First non-repeating  character is",ch)
       break
else:
    print("No non-repeating character found")
    
