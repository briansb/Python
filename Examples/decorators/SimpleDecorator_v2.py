from decorators import do_twice

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
