def function_name(*args):
    pass
#     do stuff
    return "return value 1"

def function_name_two(x,y):
    pass
#     do stuff
    return x+y

def main():
    variable1 = "something"
    variable2 = 5

    print(function_name(variable1))

    variable3 = function_name_two(3,4)
    print(variable3)

if __name__ == '__main__':
    main()
