import csv


f = open("data.csv")
# using with statement does not require close(f)
with f:
    # can specify different delimiter
    reader = csv.reader(f)
    for row in reader:
        # row is a list
        print(row)
        #for x in row:
        #    print(x)



# assuming you have a list of lists
# data = listoflists

f = open("output.csv","w")
with f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)

### or , write it all in one statement
##with f:
##    writer = csb.writer(f)
##    writer.writerows(data)

