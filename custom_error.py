
var=input("Enter the value ")
if (var=="quiz"):
    print(var)
else:
    if not var.isdigit():
        raise ValueError("Invalid!")
    elif int(var)<1 or int(var)>10:
        raise ValueError("Not a correct input")
    else:
        print(var)

