def decor(fun):
    def inner():
        return fun() * 2
    return inner

@decor
def number():
    return 10

print(number())

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello, world"

print(greet())

@decor
@uppercase_decorator
def excited_greet():
    return "hi there"

print(excited_greet())