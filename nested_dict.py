#nested dictionary of toppers in different categories
KLE={
    "school_topper":{"vinu":97,"aku":92,"kiki":90},
    "puc_topper":{"harsha":90,"aku":88,"kiki":86},
    "degree_topper":{"anu":98,"akash":86,"kirti":84}
    }
#print the full dictionary
print(KLE)
#Acess specific value
print(KLE["degree_topper"]["kirti"])

#using for loop to iterate over the dictionary
for k,v in KLE.items():
    print(k,v)

#using function to calculate total marks of student across different categories
def dict2(student_name):
    total=0
    found=False #flag
    for toppers in KLE.values():
    #Important
    #Do NOT check marks == 0 inside the loop,
    #because student might appear in next inner dict .
    #We must finish checking all categories first.
    #instead we can use flag '''

        if student_name in toppers:
            found=True
            total+=toppers[student_name]
            #marks+=toppers.get(student_name,0)  #If this student exists in this inner dictionary, gives marks else returns 0. marks stores marks 
    if not found:
        return "Student not found"
    return total

res=dict2("harsha")
print(res)
print("vinu-",dict2("vinu"))
print("kirti-", dict2("kirti"))
print("akash-", dict2("akash"))
print("anu-", dict2("anu"))
print("ojk-", dict2("ojk"))