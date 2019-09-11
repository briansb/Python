def evens(stream):
    for n in stream:
        print(f"\tgen n = {n}")
        if n % 2 == 0:
            yield n

nums = [1,2,3,4,5,6,7,8,9]
for n in evens(nums):
    print(f"n = {n}")
    
