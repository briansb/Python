# import does a copy and paste of the source in "sys"
import os

# when an import file (calling_rates.py) is not in the Python system path or current working directory
import sys
sys.path.insert(0, '/home/bbirmingham/repos/orbitalivv/cygnus/sims/SIM_CYG_ENV')
import calling_rates
# when a module is in the path
import Reservoir.testmodule


# function definitions come ahead of main...so main can find then
def function1(arg1):
    # no return value, so just call it from main
    print("In function1 with arg1 = " + str(arg1))

def function2(arg2):
    print("In function2 with arg2 = " + arg2)
    # returns a value, so must set function equal to variable in main
    return arg2 + "_revised"

def nested_list_comprehension():
    a=[]
    list1 = [1,2,3,4,5]
    list2 = [10,20,30,40,50]
    #for x in list1:
    #    for y in list2:
    #        a.append((x,y))
    # the below replaces the above 3 statements
    a = [(x,y) for x in list1 for y in list2]
    return a


# if run standalone, the system name is "__main__"
#   and so the following statements will be run.
# if imported, however, the below will not be run, but the above routines
#   will be available to the importing program
if __name__ == "__main__":
    # Concept - calling a function, no arguments
    arg1 = 43
    function1(43)

    # Concept - calling a function, arguments
    arg2 = "Test"
    var1 = function2(arg2)
    print("Return from function2 with return value = " + var1)
    # can just put the function in a print statement
    print("Quicker way of getting function2 return value =  " + function2("shorter"))

    # Concept - list comprehension
    a = nested_list_comprehension()
    print("The result of a nested list comprehension" + str(a))

    
