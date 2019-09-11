def parse_ranges(rng):
    lst = []
    for x in rng.split(','):
        if '-' not in x:
            lst.append(int(x))
        y,z = x.split('-')
        for i in range(int(y),int(z)+1):
            lst.append(i)

    return lst



def main():
    
    range1 = "1-2,4-4,8-10"
    print(parse_ranges(range1))

    range2 = "0-0, 4-8, 20, 43-45"
    print(parse_ranges(range2))

if __name__ == '__main__':
    main()
