# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x) 