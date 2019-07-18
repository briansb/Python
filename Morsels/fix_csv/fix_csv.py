import csv
from argparse import ArgumentParser

# exception will be raised if two args not given
#old_filename, new_filename = sys.argv[1:]
parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
args = parser.parse_args()


with open(args.old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    # a list comprehension that only loops (doesn't filter, modify,etc)
    #    can be replaced with the constructor
    #rows = [line for line in reader]
    rows = list(reader)
    # could combine above into rows = list(csv.reader(old_file, delimiter='|'))

with open(args.new_filename, mode='wt', newline='') as new_file:
    # condense the following two lines
    #writer = csv.writer(new_file)
    #writer.writerows(rows)
    csv.writer(new_file).writerows(rows)


# https://www.tutorialspoint.com/python/python_command_line_arguments
