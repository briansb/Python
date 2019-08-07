import subprocess

# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
##code = subprocess.call("gedit")
### must exit program for call to complete
##if code == 0:
##    print("Success")
##else:
##    print("Failure")

# with arguments
code = subprocess.call(["gedit","test.txt"])
if code == 0:
    print("Success")
else:
    print("Failure")
