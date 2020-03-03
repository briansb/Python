import time
import sys

for i in range(5):
    # Can not use print(i) since default end = '\n', which flushes the buffer
    print(i, end='')
    #sys.stdout.flush()
    time.sleep(1)