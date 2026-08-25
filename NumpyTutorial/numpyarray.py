# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))

# type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

# Example
# Get third and fourth elements from the following array and add them.
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])