
# from https://www.python-course.eu/python3_formatted_output.php

# old way
print("Art: %5d, Price per Unit: %8.2f"         %                 (453, 59.058))
#            format string             string modulo operator     tuple with values
print()

# examples
print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))
print("Only one percentage sign: %% " % ())
print("%#5X"% (47))
print("%5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("%+d"% (42))
print("% d"% (42))
print("%+2d"% (42))
print("% 2d"% (42))
print("%2d"% (42))
print()

# Even though it may look so, the formatting is not part of the print function.
# If you have a closer look at our examples, you will see that we passed a formatted string to the print function.
# Or to put it in other words: If the string modulo operator is applied to a string, it returns a string.
# This string in turn is passed in our examples to the print function.
# So, we could have used the string modulo functionality of Python in a two layer approach as well, i.e.,
# first create a formatted string, which will be assigned to a variable and this variable is passed to the print function:
s = "Price: $ %8.2f"% (356.08977)
print(s)
print()


print("The new way....")
# New way...the format method
# general form
#  template.format(p0, p1, ..., k0=v0, k1=v1, ...)
print("First argument: {0}, second one: {1}".format(47,11) )
print("Second argument: {1}, first one: {0}".format(47,11) )
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11) )
print("First argument: {}, second one: {}".format(47,11) )
# arguments can be used more than once:
print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))
# can use keyword parameters
print("Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058))
# It's possible to left or right justify data with the format method.
# Precede the formatting with a "<" (left justify) or ">" (right justify).
print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
