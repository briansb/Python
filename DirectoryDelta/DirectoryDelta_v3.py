# Import the os module, for the os.walk function
import os
 
# Set the directory you want to start from
# rootDir = '/share/bbirmingham/OrbitalMechanics'
##for dirName, subdirList, fileList in os.walk(rootDir):
##    print('Found directory: %s' % dirName)
##    for fname in fileList:
##        print('\t%s' % fname)

# this "walks" the directory structure
#rootDir = '/share/bbirmingham/OrbitalMechanics'
#for dirName, subdirList, fileList in os.walk(rootDir):
#    print(f" dirName = {dirName}, subdirList = {subdirList}, fileList = {fileList}")
    

### gets everything in rootDir
##rootDir = '/share/bbirmingham/OrbitalMechanics'
##first_level_all = os.listdir(rootDir)
##print(f" Items are {first_level_all}\n")

##rootDir = '/share/bbirmingham/OrbitalMechanics'
##filepaths = [f.path for f in os.scandir(rootDir) if f.is_file()]
##dirpaths  = [f.path for f in os.scandir(rootDir) if f.is_dir()]
##print(f" File items are {filepaths}\n")
##print(f" Dir items are {dirpaths}\n")

rootDir = '/share/bbirmingham/OrbitalMechanics'
obj = os.scandir(rootDir) 
# List all files and diretories  
# in the specified path 
print("Files and Directories in '% s':" % rootDir) 
for entry in obj : 
    if entry.is_dir() or entry.is_file(): 
        print(entry.name) 

# entry.is_file() will check 
# if entry is a file or not and 
# entry.is_dir() method will 
# check if entry is a 
# directory or not.  

# To Close the iterator and 
# free acquired resources 
# use scandir.close() method 
obj.close() 
