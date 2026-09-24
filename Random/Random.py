# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.
# Generate a random integer from 0 to 100:
from numpy import random

x = random.randint(100)

print(x) 

# Generate a 1-D array containing 5 random integers from 0 to 100:
from numpy import random

x=random.randint(100, size=(5))

print(x) 