#  This program computes the numbers that are relatively prime to 66

import cryptomath

for key in range(1,66):
    if cryptomath.gcd(key,66) == 1:
        print("%s is relatively prime to 66" % key)
