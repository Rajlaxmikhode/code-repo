def max_value(*li):
    li=list(li)
    print("list :",li)
    maximum=li[0]
    for i in li:
        if i>maximum:
            maximum=i
    print("maximum: ",maximum)

    return maximum
#max_value(21,23,11,34)
