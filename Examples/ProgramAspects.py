# Exposing various aspects/properties/functionality of a program

# Object's class name
class MyClass: pass

# Function name
def myfunc(): pass

class BaseClass: pass
class SubClass(BaseClass): pass

# Python 3 allows unicode variable names, but must be "letter-lie"
#  no emojis, etc.
#  need example...

# ----------

obj = MyClass()
print(obj.__class__.__name__)
print(myfunc.__name__)

print(issubclass(SubClass, BaseClass))
print(issubclass(SubClass, object))
print(issubclass(BaseClass, SubClass))

# ------------------
# "globals()" returns a dict
# with all global variables
# in the current scope:

>>> globals()
{...}

# "locals()" does the same
# but for all local variables
# in the current scope:

>>> locals()
{...}


