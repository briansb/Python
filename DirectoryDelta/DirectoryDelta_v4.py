import os

rootDir = '/share/bbirmingham/OrbitalMechanics'
obj = os.scandir(rootDir) 
print("Directories in '% s':" % rootDir) 
for entry in obj : 
    if entry.is_dir(): 
        print(entry.name) 

print(f"\n")

obj = os.scandir(rootDir) 
print("Files in '% s':" % rootDir) 
for entry in obj : 
    if entry.is_file(): 
        print(entry.name)
        
obj.close() 
