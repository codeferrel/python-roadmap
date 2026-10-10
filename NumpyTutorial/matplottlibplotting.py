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




# Logistic Distribution

# Logistic Distribution is used to describe growth.

# Used extensively in machine learning in logistic regression, neural networks etc.

# It has three parameters:

# loc - mean, where the peak is. Default 0.

# scale - standard deviation, the flatness of distribution. Default 1.

# size - The shape of the returned array.
from numpy import random

x = random.logistic(loc=1, scale=2, size=(2, 3))

print(x)


# Multinomial Distribution
# Multinomial distribution is a generalization of binomial distribution.
# It describes outcomes of multi-nomial scenarios unlike binomial where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
# It has three parameters:
# n - number of times to run the experiment.
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
# size - The shape of the returned array.
# Example
# Get your own Python Server

Draw out a sample for dice roll:
from numpy import random

x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])

print(x) 