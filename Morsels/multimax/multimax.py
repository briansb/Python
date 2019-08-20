def multimax(iter):
    maxi = float('-inf')

    # this doesn't handle iter = []
    # maxi = max(iter)
    for x in iter:
        if x > maxi:
            maxi = x
    
    return [x for x in iter if x == maxi]


def main():
    
    variable1 = [1,2,3,4]
    
    variable2 = [1,4,2,4,3]

    variable3 = (1,1,1)

    variable4 = []

    print(multimax(variable1))

    print(multimax(variable2))

    print(multimax(variable3))

    print(multimax(variable4))
    

if __name__ == '__main__':
    main()
