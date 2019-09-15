def another_function(func):

##    def other_func():
##        val = "The result of %s is %s" % (func(), eval(func()))
##        return val
##    return other_func
    
#      this doesn't work because you have to return a function
#      the commented lines above return a function
       val = "The result of %s is %s" % (func(), eval(func()))
       return val

@another_function
def a_function():
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)
