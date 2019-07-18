handle = open("test.txt", "r")

# reads contents into data as a giant string
data = handle.read()

# reads one line
# data = handle.readline()

# returns a list
# data = handle.readlines()

print(data)
handle.close()
