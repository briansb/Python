#  https://www.machinelearningplus.com/python/parallel-processing-python/
import time
import multiprocessing as mp
import numpy as np

print(f"Number of processors: {mp.cpu_count()}")

# Synchronous execution - processes are completed in the same order in which they were started
#     This will lock the main program until processes are finished
#   Pool.map() and Pool.starmap()
#   Pool.apply()

# Asynchronous execution - No locking, but finish order is not guaranteed.  Usually quicker
#    Pool.map_async() and Pool.starmap_async()
#    Pool.apply_async()

# Problem - how many numbers are present, in a given range, in each row?
# Prepare data - a 2D matrix (or list of lists)
# change number of rows to 200000
numberofrows = 5000000

# sets the random seed without impacting the global numpy state...whatever that means
np.random.RandomState(100)
# returns an array of random integers, range 0 to 10, with shape [rows,5]
arr = np.random.randint(0, 10, size=[numberofrows, 5])
# converts the array into a list
data = arr.tolist()
# these two statements need to be swapped for large numberofrows
#print(f"Data = {data}")
print(f"Data = {data[:10]}")
print()

lower = 4
upper = 8
print(f"In the above array of lists, the numbers are random, 0 -> 9")
print(f"Problem: For each row (list), how many numbers lie between {lower} and {upper}?")

print("Beginning slow solution")
start = time.time()
# Solution without parallelization
def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

results = []
for row in data:
    results.append(howmany_within_range(row, minimum=lower, maximum=upper))
end = time.time()
# swap for large numberofrows
#print(f"Solution = {results}")
print(f"Solution = {results[:10]}")
print(f"Elapsed time = {(end - start):.6f}")
