# Obtaining Boolean Array from binary array
# Problem : Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array

import numpy as np

a = np.array([0, 1, 0, 1, 0])
b = a.astype('bool')
print(b)