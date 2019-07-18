class Circle(object):
    def __init__(self, n = 0):
        if n == 0:
            n = 1
        self.radius = n

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, val):
        if val < 0:
            raise Exception('Radius cannot be negative')
        self._radius = val
        self._diameter = 2.0 * val
        self._area = 3.14159 * val * val


    @property
    def diameter(self):
        return self._diameter
    
    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2.0
        self.area = 3.14159 * val * val / 4.0
        
        
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, val):
        raise Exception('Cannot set attribute area')
        

#c = Circle()
#print(c.radius)
#print(c.diameter)
#print(c.area)

#c = Circle(5)
#print(c.radius)
#print(c.diameter)
#print(c.area)

#c.radius = 6
#print(c.radius)
#print(c.diameter)
#print(c.area)

##c.area = 5

#c.radius = -3


