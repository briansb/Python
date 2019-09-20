# Exposing various aspects/properties/functionality of a program

# Object's class name
class MyClass: pass

# Function name
def myfunc(): pass

class BaseClass: pass
class SubClass(BaseClass): pass

# ----------

obj = MyClass()
print(obj.__class__.__name__)
print(myfunc.__name__)

print(issubclass(SubClass, BaseClass))
print(issubclass(SubClass, object))
print(issubclass(BaseClass, SubClass))


