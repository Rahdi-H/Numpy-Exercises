# Array Generation by repeatition of a small array across each dimension
# Problem : Output an array by repeating a smaller array of 2 dimensions, 10 times
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.tile(a, 10)
print(b)