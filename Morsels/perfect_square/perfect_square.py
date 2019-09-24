import math
import numbers

def is_perfect_square(n):
    if not isinstance(n, numbers.Number):
        raise TypeError(f"{n} is NOT a number")
        
    root = math.sqrt(n)
    x = math.floor(root)
    if x == root:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_perfect_square([1,2,3]))
    print(is_perfect_square(225))
    print(is_perfect_square(40))
    print(is_perfect_square(16))
    print(is_perfect_square("bb"))



