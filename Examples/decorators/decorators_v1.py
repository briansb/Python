# functions are first-class objects...
#   meaning they can be used as objects...
#   stored, compared, passed as argument, etc
def say_hello(name):
    return(f"Hello {name}")

def be_awesome(name):
    return(f"Yo {name}, together we are the awesomest!")

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))
print()

# inner functions
def parent(num):
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    def third_child():
        print("Third function")
        
    if num == 3:
        return third_child
    
    second_child()
    first_child()

# Can not call first_child or second_child from here - not in scope
#  Additionally, not created until parent() is called
parent(0)
print()

# will return third_child as address
third = parent(3)
# function called WITHOUT parentheses...sending address only
print(third)
# will execute third_child
# function called WITH parentheses...function is to be executed
print(third())
