# Custom sequence Generation
# Problem : Generate a sequence of numbers in the form of a numpy array from 0 to 100 with gaps of 2 numbers, for example: 0, 2, 4 ....
import numpy as np

list_of_numbers = [i for i in range(0, 101, 2)]
a = np.array(list_of_numbers)
print(a)