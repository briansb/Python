#  https://www.machinelearningplus.com/python/parallel-processing-python/

import multiprocessing as mp

print(f"Number of processors: {mp.cpu_count()}")

# Synchronous execution - processes are completed in the same order in which they were started
#     This will lock the main program until processes are finished
#   Pool.map() and Pool.starmap()
#   Pool.apply()

# Asynchronous execution - No locking, but finish order is not guaranteed.  Usually quicker
#    Pool.map_async() and Pool.starmap_async()
#    Pool.apply_async()

import numpy as np
from time import time

# Problem - how many numbers are present, in a given range, in each row?
# Prepare data - a 2D matrix (or list of lists)
# change numberofrows to 200000
numberofrows = 10

# sets the random seed without impacting the global numpy state...whatever that means
np.random.RandomState(100)
# returns an array of random integers, range 0 to 10, with shape [rows,5]
arr = np.random.randint(0, 10, size=[numberofrows, 5])
# converts the array into a list
data = arr.tolist()
print(data[:5])


# Solution without parallelization

