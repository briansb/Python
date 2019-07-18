# this was my solution
# def get_earliest(*args):
#     earliest = args[0]
#     for i in range(1,len(args)):
#         earliest = get_two(earliest,args[i])
#     return earliest
#
# def get_two(x,y):
#     a = x.split('/')
#     b = y.split('/')
#     for n in [2,0,1]:
#         if a[n] == b[n]:
#             continue
#         else:
#            if a[n] > b[n]:
#                return y
#            else:
#                return x

# preferred solution - using tuple unpacking
# whenever you see literal indexes, a[3] or array[0],
#   think of tuple unpacking
# def get_earliest(date1, date2):
#     m1, d1, y1 = date1.split('/')
#     m2, d2, y2 = date2.split('/')
#     if (y1, m1, d1) < (y2, m2, d2):
#         return date1
#     else:
#         return date2

# now for the multiple dates
def get_earliest(*)


def main():
    first = "03/21/1946"
    second = "02/24/1946"
    third = "06/15/1958"
    print(get_earliest(first, second))

if __name__ == '__main__':
    main()
