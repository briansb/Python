import sys

def function_name(*args):
    pass
#     do stuff
    return "return value 1"

def function_name_two(x,y):
    pass
#     do stuff
    return x+y

def main():

    wordinquestion = sys.argv[1]

    for char in wordinquestion:
        print(char)



#    print(f"Number of arguments: {len(sys.argv)} arguments.")
#    print(f"Argument List: {str(sys.argv)}")
# 
#    variable1 = "something"
#    variable2 = 5

#    print(f"{function_name(variable1)}")

#    variable3 = function_name_two(3,4)
#    print(variable3)

if __name__ == '__main__':
    main()




