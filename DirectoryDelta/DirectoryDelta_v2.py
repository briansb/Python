import os

folder = '.'
filepaths = [os.path.join(folder, f) for f in os.listdir(folder)]

print(f"filepaths = {filepaths}")