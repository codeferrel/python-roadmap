# Data Distribution
# Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.
# In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.
# How Can we Get Big Data Sets?
# # To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.

# EX : Create an array containing 250 random floats between 0 and 5:
import numpy

x = numpy.random.uniform(0.0, 5.0, 250)

print(x) 



# Use the NumPy percentile() method to find the percentiles:

import numpy

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = numpy.percentile(ages, 75)

print(x)