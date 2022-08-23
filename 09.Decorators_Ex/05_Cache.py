def cache(func_ref):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]
        result = func_ref(number)
        log[number] = result

        return result

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
