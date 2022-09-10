# Array Generation of random integers within a specified range
# Problem : Output a 5-by-5 array of random integers between 0 (inclusive) and 10 (exclusive)
import numpy as np
np.random.seed(123)
a = np.random.randint(0, 10, size=(5, 5))
print(a)