# Getting the positions (indexes) where elements of 2 numpy arrays match
# Problem : From 2 numpy arrays, extract the indexes in which the elements in the 2 arrays match
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([9, 8, 7, 4, 5])

c = np.where(a == b)
print(c)