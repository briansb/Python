import os

# gets everything in directory
first_path = "/share/bbirmingham/Odyssey/"
first_list = os.listdir(first_path)
print(f" Items are {first_list}")

# grabs just the files in first_path
onlyfiles = [f for f in first_list if os.path.isfile(os.path.join(first_path, f))]
print(f" Files are {onlyfiles}")
print(f"  ")


# ?
f = []
for (dirpath, dirnames, filenames) in os.walk(first_path):
    f.extend(filenames)
    print(f" dirpath = {dirpath}")
    print(f" dirnames = {dirnames}")
    print(f" filenames = {filenames}")
    print(" ")
    # uncomment break for top directory only
    # break

print(f"Finished")
print(f" dirpath = {dirpath}")
print(f" dirnames = {dirnames}")
print(f" filenames = {filenames}")
