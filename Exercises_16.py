# Matrix Multiplication 
# Problem : Given 2 numpy arrays as matrices, output the result of multiplying the 2 matrices (as a numpy array)
import numpy as np
a = np.array([[1, 2], [4, 5]])
b = np.array([[7, 8], [10, 11]])
c = np.matmul(a, b)
print(c)