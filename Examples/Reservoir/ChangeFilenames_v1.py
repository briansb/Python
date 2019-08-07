import os
import random
import sys
from shutil import copyfile
import collections

def get_subdirs(dir):
    "Get a list of immediate subdirectories"
    return next(os.walk(dir))[1]

def get_subfiles(dir):
    "Get a list of immediate subfiles"
    return next(os.walk(dir))[2]

def get_fileprefix(index,lst):
    "Get the next file prefix"
    if index > len(lst) -1 :
        print("A bad thing has happened")
        sys.exit()
    # add leading zeros to prefix
    return str(lst[index]).zfill(5)


parentdirectory = "D:\Photographs in Digital Frame"
# L is the current USB port
newdestination = "L:"

# Get total number of files and folders
numfiles = numfolders = 0
for _, dirnames, filenames in os.walk(parentdirectory):
  # ^ this idiom means "we won't be using this value"
    numfiles += len(filenames)
    numfolders += len(dirnames)
# print("{:,} files, {:,} folders".format(numfiles, numfolders))
print("Found " + str(numfiles) + " to copy")

# We will be using a 5 digit random number as the prefix of the newfilename
# So, we generate 'numfiles' random numbers over a range of 1 to 99999
prefixlist = random.sample(range(1, 99999), numfiles)
#print(prefixlist)

# build dictionary of old filenames and new filenames
os.chdir(parentdirectory)
directorylist = get_subdirs(".")
listindex = 0
filedictionary = dict()
for directory in directorylist:
    os.chdir(directory)
    #print("Working with directory " + directory)
    filelist = get_subfiles(".")
    for fyle in filelist:
        # build complete path for old filename
        oldfilename = parentdirectory + "\\" + directory + "\\" + fyle
        #build complete path for new filename
        filename, file_extension = os.path.splitext(fyle)
        newfilename = newdestination + get_fileprefix(listindex,prefixlist) + "_" + filename + "_" + directory + file_extension
        listindex += 1
        filedictionary[newfilename] = oldfilename
        #print("       " + oldfilename + " becomes " + newfilename)
    os.chdir(parentdirectory)

sorted_dict = collections.OrderedDict(sorted(filedictionary.items()))

# print dictionary
for key in sorted_dict:
    #print(key + " <- " + sorted_dict[key])
    print("Copying " + sorted_dict[key] + " to " + key)
    copyfile(sorted_dict[key], key)
