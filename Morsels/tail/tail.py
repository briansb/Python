def tail(sequence, n):

# my solution
##    lst = []
##    if n > len(sequence):
##        print("n is greater than the sequence length")
##        return lst
##    for x in range(len(sequence) - n, len(sequence)):
##        lst.append(sequence[x])

# his solution
    if n <= 0:
        return []
    return list(sequence[-n:])

### for large iterables
##    items = []
##    if n <= 0:
##        return []
##    for item in iterable:
##        items = [*items[-(n-1):], item]
##        # the asterisk unpacks the last (n-1) items into a new list,
##        #    with current item at the end
##    return items


def function_name_two(x,y):
    pass
#     do stuff
    return x+y

def main():
    variable1 = "something"
    variable2 = [5,4,3,2,1]
    variable3 = (17, 19, 23, 29)

    print(tail(variable1, 4))
    #print(variable1[4])
    print("")
    print(tail(variable2, 3))
    #print(variable2[3])
    print("")
    print(tail(variable3, 2))
    #print(variable3[2])



if __name__ == '__main__':
    main()
