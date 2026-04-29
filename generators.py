def funn():
    yield 'rock'
    yield  'paper'
    yield  'stone'

demo=funn()
print(next(demo))
print(next(demo))
print(next(demo))


# Without generator
squares = []
for i in range(5):
    squares.append(i*i)
print("Without generator: ",squares)

# With generator
powers = (i**i for i in range(5))
print("Using generator:",list(powers))