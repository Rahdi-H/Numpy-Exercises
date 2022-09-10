# Array Re-Dimensioning
# Problem : Convert a 1-D array to a 3-D array

import numpy as np

a = np.array([i for i in range(27)])

b = a.reshape((3, 3, 3))
print(b)