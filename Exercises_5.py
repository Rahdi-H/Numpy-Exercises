# Array Data-type Conversion
# Problem : Convert all the elements of a numpy array from float to integer datatype

import numpy as np

a = np.array([2.1, 1.5, 6.25, 4.33])
b = a.astype('int')
print(b)