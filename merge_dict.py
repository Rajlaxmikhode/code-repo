dict1={"India":"Delhi","UsA":"Washington","England":"London","France":"Paris"}
dict2={"Karnataka":"Banglore","Maharastra":"Mumbai","UP":"Lucknow","Tamil nadu":"Chennai"}
dict1.update(dict2)
print(dict1)
#if both dict have same keys it will dict2 overwrites dict1..
print("using '|-union operator' ")
merge=dict1|dict2
print(merge)