import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


# Uniform Distribution
# Used to describe probability where every event has equal chances of occuring.
# E.g. Generation of random numbers.
# It has three parameters:
# low - lower bound - default 0.0
# high - upper bound - default 1.0
# size - The shape of the returned array
from numpy import random

x = random.uniform(size=(2, 3))

print(x)