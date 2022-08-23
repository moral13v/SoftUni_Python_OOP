def even_parameters(function):
    def wrapper(*args):
        for el in args:
            if not isinstance(el, int) or el % 2 != 0:
                return "Please use only even numbers!"
        return function(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
