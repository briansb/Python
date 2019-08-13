import sys
import subprocess

# run from the command line, sys.argv returns the parameters
print(sys.argv)

# path to Python executable
print(sys.executable)

# call a program that calls exit
code = subprocess.call(["python", "exit.py"])
print(f"Exit code = {code}")

