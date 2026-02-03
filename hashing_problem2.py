

def frequency(arr):
    dic={}

    for i in arr:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic
           
print(frequency([1, 2, 2, 3, 1, 1, 2, 4]))