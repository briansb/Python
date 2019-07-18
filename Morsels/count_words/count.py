# mine
#def count_words(my_string):
#    x = {}
#    wordlist = my_string.lower().split(' ')
#    for word in wordlist:
#        # do some processing
#        if word in x:
#            x[word] += 1
#        else:
#            x[word] = 1
#
#    return x

def count_words(my_string):
    x = {}
    for word in my_string.lower().split(' '):
        x[word] = x.get(word, 0) + 1

    return x


def main():
    target = "some Value of this should give a value Of something"
    print(count_words(target))

if __name__ == '__main__':
    main()
