import os

# open a file that is in the same folder as this script
handle = open("test.txt")
# close file
handle.close()

# open a file by specifying its full path, and read_only mode
handle = open(os.getcwd() + "/test.txt", "r")
handle.close()

# open the file in read-only binary mode
handle = open("test.pdf", "rb")
handle.close()

# open a file in read-only mode
handle = open("test.txt", "r")
# read the contents into 'data' as a giant string
data = handle.read()
# print it out
print(data)
handle.close()


# reads one line
handle = open("test.txt", "r")
data = handle.readline()
print(data)

# returns a list
data = handle.readlines()
print(data)
handle.close()

# # file modes
##r - Open text file for reading.  Will overwrite.  The stream is positioned at the beginning of the file.
##r+ - Open for reading and writing.  Will overwrite.  The stream is positioned at the beginning of the file.
##w - Truncate to zero length or create text file for writing.  Will overwrite.  The stream is positioned at the beginning of the file.
##w+ - Open for reading and writing.  Will overwrite.  The file is created if it does not exist, otherwise it is truncated.  The stream is positioned at the beginning of the file.
##a - Open for writing.  Will append.  The file is created if it does not exist.  The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.
##a+ - Open for reading and writing.  Will append.  The file is created if it does not exist.  The stream is positioned at the end of the file.  Subsequent writes to the file will always end up at the then current end of file, irrespective of any intervening fseek(3) or similar.


# add this preferred file handling method:
print("\n\nPreferred method of file handling")
with open("test.txt") as file:
    # do some file processing
    for line in file:
       print(line, end="")
# at this point, file is closed.  No need for file.close()

# more detailed:

# try:
#     with open( "a.txt" ) as f :
#         print f.readlines()
# except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available
#     print 'oops'

# If you want different handling for errors from the open call vs the working code you could do:

# try:
#     f = open('foo.txt')
# except IOError:
#     print('error')
# else:
#     with f:
#         print f.readlines()



# handle = open("test.txt", "r")
# data = handle.readline() # read just one line
# print(data)
# handle.close()

# handle = open("test.txt", "r")
# data = handle.readlines() # read ALL the lines!
# print(data)
# handle.close()

# # open and read the file using the with operator
# with open("test.txt") as file_handler:
#     for line in file_handler:
#         print(line)

# # read in chunks
# handle = open("test.txt", "r")
# while True:
#     data = handle.read(1024)
#     print(data)
#     if not data:
#         break

# handle = open("test.txt", "r")
# for line in handle:
#     print(line)
# handle.close()
