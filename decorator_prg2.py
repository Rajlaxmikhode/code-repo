
#Decorators are functions that take another function as an argument and return a new function that extends or modifies the behavior of the original function.
def greet(fn):
    def fun(name):
        print("This is BCA college")
        fn()
        print(f"Thanks for coming, {name}")
        
    return fun

@greet
def hello():
    print("Welcome")

hello("ma'am")
