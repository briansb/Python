def do_twice(func):
    # added *args, **kwargs to allow any number of args...from 0 to n
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


