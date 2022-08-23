def logged(function):
    def wrapper(*args):
        func_name = function.__name__
        func_result = function(*args)

        return f"you called {func_name}{args}\n" \
               f"it returned {func_result}"
    return wrapper


@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))


