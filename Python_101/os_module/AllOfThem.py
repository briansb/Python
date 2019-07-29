import os
import subprocess, sys  # for use with subprocess
print("Platform is {0}".format(os.name))

# will return an error if DESTOP_SESSION not present
print(f"Desktop session is {os.environ['DESKTOP_SESSION']}")

# will return None if not present
print(f"Path is {os.getenv('PATH2')}")

# change directory, get current working directory
os.chdir("/home/user/Python/Python_101/os_module")
print(os.getcwd())

# make a directory
os.mkdir("/home/user/TempDir")
# make a path of directories
path = "/home/user/Temp2Dir/Brian"
os.makedirs(path)

# delete files and directories
os.rmdir("/home/user/TempDir")
os.rmdir("/home/user/Temp2Dir/Brian")
os.rmdir("/home/user/Temp2Dir")

# create file
f = open("test.txt", mode = "w")
f.close()
# rename file
os.rename("test.txt","test_one.txt")

# replaces os.startfile on Linux
#opener ="open" if sys.platform == "darwin" else "xdg-open"
#subprocess.call(["xdg-open", "test_one.txt"])

# delete file
os.remove("test_one.txt")

# iterates over all directories and paths in argument
for root, dirs, files in os.walk("/home/user/Python/Python_101"):
    # all of the paths
    print(root)
    for _dir in dirs:
        # all of the directories in the loop iterator 'root'
        print("\t" + _dir)
##        for _file in files:
##            print("\t\t" + _file)
