# Generating the array element indexes such that the array elements appear in ascending order
# Problem : Output the array element indexes such that the array elements appear in the ascending order
import numpy as np
a = np.array([5, 7, 2, 6])
b = np.argsort(a)
print(b)