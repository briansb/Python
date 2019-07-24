import os

print("Platform is {0}".format(os.name))

# will return an error if DESTOP_SESSION not present
print(f"Desktop session is {os.environ['DESKTOP_SESSION']}")

# will return None if not present
print(f"Path is {os.getenv('PATH2')}")

# change directory, get current working directory
os.chdir("/home/user/Linux")
print(os.getcwd())

# make a directory
os.mkdir("/home/user/TempDir")
# make a path of directories
path = "/home/user/Temp2Dir/Brian/Birmingham/Beth/Brooks"
os.makedirs(path)

