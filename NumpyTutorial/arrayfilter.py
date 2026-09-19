# If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
import numpy as np

arr = np.array([41, 42, 43, 44])

x = arr[[True, False, True, False]]

print(x)
