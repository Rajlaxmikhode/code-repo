while True:
    try:
        a=int(input("Enter the value of a: "))
        b=int(input("Enter the value of b: "))
        c=a/b
    except ValueError:
        print("Enter a valid integer only")

    except ZeroDivisionError:
        print("Divide by zero error")
    else:
        print("C:",c)
        break
    finally:
        print("I am always executed")# This block always executes whether an exception occurs or not


#In this example, it demonstrates behavior, but in real-world code, finally is mainly used for cleanup operations like closing files, database connections, or releasing resources.