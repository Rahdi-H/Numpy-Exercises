# Element-wise addition of 2 numpy arrays

# Problem : Given are 2 similar dimensional numpy arrays, 
# how to get a numpy array output in which every element is an element-wise sum of the 2 numpy arrays?

import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
b = np.array([[9, 10, 11, 12], [13, 14, 15, 16]])

c = a + b

print(c)