haystack = range(0,10)
needle = 11

# Pythonic way of checking for membership
if needle not in haystack:
    raise ValueError('Needle not found')
