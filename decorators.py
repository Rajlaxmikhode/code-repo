#Decorators are functions that take another function as an argument and return a new function that extends or modifies the behavior of the original function.
def greet(fn):
    def fun():
        print("This is BCA college")
        fn()
        print("Thanks for coming")
    return fun
def hello():
    print("Welcome")

hello=greet(hello)
hello()
