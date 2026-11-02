# Matplotlib Plotting
Draw a line in a diagram from position (1, 3) to position (8, 10):
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()