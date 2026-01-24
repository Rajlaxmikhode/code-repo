def avg(*num):
        sum=0
        for i in num:
                sum+=i
        return (sum)/len(num)
print(avg(8,5,3,2,))