import math

class Circle:
    # initializer method
    def __init__(self, radius = 1):
        self.radius = radius
        #self.area = math.pi * self.radius ** 2
        #self.diameter = self.radius * 2

    # string representation
    def __repr__(self):
        return f'Circle({self.radius})'

    # turns attributes into properties
    #  equivalent to a getter method
    #  called a decorator
    @property
    def diameter(self):
        return self.radius * 2

    #  equivalent to setter method
    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

        

    @property
    def area(self):
        return math.pi * self.radius ** 2


    # to handle setting the radius AND
    #  making sure it's not negative
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius
    


c = Circle(5)
print(c)
print(c.radius)
print(c.diameter)
print(c.area)
print()

c.diameter = 50
print(c.radius)
print(c.diameter)
print(c.area)
print()

c.radius = 10
print(c.radius)
print(c.diameter)
print(c.area)
print()

c.radius = -10
