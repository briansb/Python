# First, we need to do some setup work. We'll import the "collections" and the "multiprocessing" module so we can use Python's parallel computing facilities and define the data structure we'll work with:
import collections
import multiprocessing

# Second, we'll use "collections.namedtuple" to define a new (immutable) data type we can use to represent our data set, a collection of scientists:
Scientist = collections.namedtuple('Scientist', [
    'name',
    'born',
])

scientists = (
    Scientist(name='Ada Lovelace', born=1815),
    Scientist(name='Emmy Noether', born=1882),
    Scientist(name='Marie Curie', born=1867),
    Scientist(name='Tu Youyou', born=1930),
    Scientist(name='Ada Yonath', born=1939),
    Scientist(name='Vera Rubin', born=1928),
    Scientist(name='Sally Ride', born=1951),
)

# Third, we'll write a "data processing function" that accepts a scientist object and returns a dictionary containing the scientist's name and their calculated age: 
def process_item(item):
    return {
        'name': item.name,
        'age': 2017 - item.born
    }
#The process_item() function just represents a simple data transformation to keep this example short and sweet—but you could swap it out with a much more complex computation no problem. 

# Fourth, and this is where the real parallelization magic happens, we'll set up a "multiprocessing pool" that allows us to spread our calculations across all available CPU cores. 
# Then we call the pool's map() method to apply our process_item() function to all scientist objects, in parallel batches:

pool = multiprocessing.Pool()
result = pool.map(process_item, scientists)
# Note how batching and distributing the work across multiple CPU cores, performing the work, and collecting the results are all handled by the multiprocessing pool. How great is that?

print(tuple(result))
