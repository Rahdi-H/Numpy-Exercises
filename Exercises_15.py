# Array Generation of random numbers following normal distribution
# Problem : Output a 3-by-3 array of random numbers following normal distribution
import numpy as np

np.random.seed(159)
a = np.random.normal(size=(5, 5))
print(a)