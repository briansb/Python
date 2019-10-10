import functools

def do_twice(func):
    # added *args, **kwargs to allow any number of args...from 0 to n
    # preserves identity
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        #  replace above with
        #return func(*args, **kwargs)
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")
    
say_whee()

@do_twice
def greet(name):
    print(f"Hello {name}")

greet("Bob")
print(greet("Bob"))
# print statement is printing None because decorator do_twice
#    does not explicitly return a value
#  see decorators.py
