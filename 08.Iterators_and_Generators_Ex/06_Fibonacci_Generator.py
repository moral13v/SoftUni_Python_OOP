def fibonacci():
    first = 0
    second = 1
    while True:
        yield first
        result = first + second
        first = second
        second = result


generator = fibonacci()
for i in range(5):
    print(next(generator))



