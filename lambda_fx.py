#lambda function to add two numbers
add = lambda x, y: x + y
print(add(3, 4))

#lambda function to convert celsius to fahrenheit
celsius_to_fahrenheit = lambda c: (c*9/5) + 32
print(celsius_to_fahrenheit(273.12))

#using function as argument
def fun(fx):
    return 10 * fx(12, 4)

print(fun(add))