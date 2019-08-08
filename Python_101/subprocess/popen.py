import subprocess

##program = "gedit"
##process = subprocess.Popen(program)
### causes program to suspend until 'program" exits
##code = process.wait()
##
##print(f"Return process {process}")
##print(f"Return code {code}")

# will return the result of ls -l into data
# puts stdout, then stderror into data
args = ["ls", "-l"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
for line in data:
    print(line)

