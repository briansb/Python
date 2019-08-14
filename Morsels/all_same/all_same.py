def all_same(seq):
# assumes all sequence values are hashable
    x = seq[0]
    print(hash(x))
    for x in seq[1:]:
        print(hash(x))
    # or return false
    return True

def main():
    variable1 = [1,1,1]
    variable2 = [1,0,1]
    variable3 = [(1,'a'),(1,'a')]
    variable4 = [(1,'a'),(1,'b')]

    print(all_same(variable1))
    print(all_same(variable2))
    print(all_same(variable3))
    print(all_same(variable4))


if __name__ == '__main__':
    main()
