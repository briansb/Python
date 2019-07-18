handle = open("test.txt", "r")

# reads contents into data as a giant string
data = handle.read()

# reads one line
# data = handle.readline()

# returns a list
# data = handle.readlines()

print(data)
handle.close()

# -----  more


add this preferred file handling method:

with open("text.txt") as file:
    # do some file processing
    # example
    for line in f:
        print(line, end="")
# at this point, file is closed.  No need for file.close()

more detailed:

try:
    with open( "a.txt" ) as f :
        print f.readlines()
except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
    print 'oops'

If you want different handling for errors from the open call vs the working code you could do:

try:
    f = open('foo.txt')
except IOError:
    print('error')
else:
    with f:
        print f.readlines()
