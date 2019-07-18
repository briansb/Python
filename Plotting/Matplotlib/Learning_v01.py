#   https://realpython.com/python-matplotlib-guide/
#  Python Plotting with matplotlib
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(444)
fig = plt.figure()
fig.suptitle('No axes on this figure')
fig, ax_lst = plt.subplots(2,2)
