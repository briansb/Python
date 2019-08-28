class Point:
    def __init__(self, x_coord, y_coord, z_coord):
        self.x = x_coord
        self.y = y_coord
        self.z = z_coord

    def __repr__(self):
        rstring = f"Point(x={self.x}, y={self.y}, z={self.z})"
        return rstring

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x == other.x) & (self.y == other.y) & (self.z == other.z)
        return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point(x,y,z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Point(x,y,z)



def main():

    x = Point(3, 4, 5)
    print(x)

    y = Point(3,4,5)
    print(y)

    print(x==y)

    y.y = 10
    print(y)
    print(x==y)

    z = x + y
    print(z)

    u = x-y
    print(u)
    
if __name__ == '__main__':
    main()
