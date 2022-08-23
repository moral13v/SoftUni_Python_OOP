def tags(param):
    def decorator(func_ref):
        def wrapper(*args):
            return f"<{param}>{func_ref(*args)}</{param}>"
        return wrapper
    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
print()


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
