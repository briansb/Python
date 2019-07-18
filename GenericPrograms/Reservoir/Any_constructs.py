

if any (e for e in [1, 2, 'joe'] if isinstance(e, int) and e > 0):
  print("True...or found one")
else:
  print("False...did not find one")

z = [ 10, 20, 30 ]
if any ( [ x > 10 for x in z ] ):
    print('True')
else:
    print('False')


a = [2,3,4,5,6,7,8,9,0]
xyz = [0,12,6,4,242,7,9]
for x in xyz:
    if x in a:
        print(x)

print("")

print([x for x in xyz if x in a])

if any (x for x in xyz if x in a):
    print("Something is true")
else:
    print("Nothing is true")

if all (x for x in xyz if x in a):
    print("Everything is true")
else:
    print("Something is false")

print([x for x in xyz if x in a and x > 5])
