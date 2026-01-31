def find_max(*li):
    li=list(li)
    print("list :",li)
    maximum=li[0]
    for i in li:
        if i>maximum:
            max=i
    print("maximum: ",maximum)

    return maximum
find_max(21,23,11,34)


