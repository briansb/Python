def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

print(say_whee)
say_whee()

say_whee = my_decorator(say_whee)
# the decoration happens here
# say_whee has been "decorated" by my_decorator
# or more accurately, it has been wrapped
# IMPORTANT:  say_whee is no longer the address of say_whee()
#             say_whee is the address of the wrapper above

print(say_whee)
say_whee()
