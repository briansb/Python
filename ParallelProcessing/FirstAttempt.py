# Below does not work....try this
#  https://www.machinelearningplus.com/python/parallel-processing-python/
# or this....


##A good simple way to start with parallel processing in python is just the pool mapping in mutiprocessing -- its like the usual python maps but individual function calls are spread out over the different number of processes.
##
##Factoring is a nice example of this - you can brute-force check all the divisions spreading out over all available tasks:
##
##from multiprocessing import Pool
##import numpy
##
##numToFactor = 976
##
##def isFactor(x):
##    result = None
##    div = (numToFactor / x)
##    if div*x == numToFactor:
##        result = (x,div)
##    return result
##
##if __name__ == '__main__':
##    pool = Pool(processes=4)
##    possibleFactors = range(1,int(numpy.floor(numpy.sqrt(numToFactor)))+1)
##    print 'Checking ', possibleFactors
##    result = pool.map(isFactor, possibleFactors)
##    cleaned = [x for x in result if not x is None]
##    print 'Factors are', cleaned


# ---- May want to lose this -----
# Here's an end-to-end example of parallel computing in Python 2/3,
#    using only tools built into the Python standard library

# First, setup.  Import "collections" and "multiprocessing" modules.
import collections
import multiprocessing

# Second, use "collections.namedtuple" to define a new (immutable) data type
#    that we can use to represent our data set, a collection of scientists.
Scientist = collections.namedtuple('Scientist', ['name', 'born'])
scientists = (
    Scientist(name='Ada Lovelace', born=1815),
    Scientist(name='Emmy Noether', born=1882),
    Scientist(name='Marie Curie', born=1867),
    Scientist(name='Tu Youyou', born=1930),
    Scientist(name='Ada Yonath', born=1939),
    Scientist(name='Vera Rubin', born=1928),
    Scientist(name='Sally Ride', born=1951)
)

# Third, write a "data processing function" that accepts a scientist object
#    and returns a dictionary containing the scientist's name and their calculated age.
#    The process_item() function represents a data transformation to keep this short.
#    Could use a much more complex computation. 
def process_item(item):
    return {'name': item.name, 'age': 2017 - item.born}

# Fourth (this is where the real parallelization magic happens), set up a "multiprocessing pool"
#    that allows us to spread our calculations across all available CPU cores. 
#    Then we call the pool's map() method to apply our process_item() function to all scientist objects,
#    in parallel batches.
#    Note how batching and distributing the work across multiple CPU cores, performing the work,
#    and collecting the results are all handled by the multiprocessing pool. 
pool = multiprocessing.Pool(multiprocessing.cpu_count())
print("Before result")
result = pool.map(process_item, scientists)
pool.close()

print("Got here")
# Fifth, show results
print(scientists)
print(process_item(scientists[2]))
print(result)
#print(tuple(result))


