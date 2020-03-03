import argparse

# this is the simplest case
# parser = argparse.ArgumentParser()
# parser.parse_args()
# run with just the above three lines plus -h/--help for basic info, $ python ArgumentParsing.py -h

# add a positional argument
# parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here")
# args = parser.parse_args()
# print("The argument = " + args.echo)
# run with $ python ArgumentParsing.py thisisatest
# argparse treats all arguments as strings, unless specified

# add an integer argument
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print("The square = " + str(args.square**2))
# run with $ python ArgumentParsing.py 4

# add an optional argument
# the two-dash (or one-dash) is the optional indicator
# parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
#  now, verbosity is a flag...if --verbosity is specified, the flag is true...pyton ArgumentParsing.py --verbosity
#     if verbosity is not specified, the flag is false
# args = parser.parse_args()
# if args.verbosity:
#    print("verbosity turned on")

# short options
# parser = argparse.ArgumentParser()
# parser.add_argument("-v", "--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

# combining positional and optional arguments
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
else:
    print(answer)