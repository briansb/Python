import sys
import subprocess

# run from the command line, sys.argv returns the parameters
print(sys.argv)

# path to Python executable
print(sys.executable)

# call a program that calls exit
code = subprocess.call(["python", "exit.py"])
print(f"Exit code = {code}")

# the search path for modules.  This is NOT the system PATH variable
#  this is PYTHONPATH
print(f"The system path is \n{sys.path}")
sys.path.append("/home/usr/anotherpath")
print(f"The appended system path is \n{sys.path}")
sys.path.remove("/home/usr/anotherpath")
print(f"The system path is \n{sys.path}")

# the platform
print(f"The OS platform is {sys.platform}")

# can redirect stdin, stdout, stderr
original = sys.stdout
sys.stdout = open('temporary_stdout.txt', 'w')
print('This is your redirected text:')
sys.stdout = original
print('Back to normal')
