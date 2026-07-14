def avg(*num):
        sum=0
        for i in num:
                sum+=i
        return (sum)/len(num)
numbers=list(map(int, input("Enter numbers to find average").split()))
print(avg(*numbers)) 