# A numpy array is a grid of values with the same type and is indexed by a tuple of non-negative values.
# Numpy arrays have the type of ndarray.
# Use the array() function to create a numpy array.
# Use the dtype property to get the data type of array’s elements.
# Use the ndim property to get the number of dimensions or the number of axes.
# Use the shape property to get the number of dimensions as well as the number of elements in each dimension.

import os

file_path = os.path.join('Array_Indexing&Slicing', 'indexing.py')
with open(file_path, 'r') as file:
    import numpy as np

    a = np.arange(0, 5)
    print(a)

    print(a[0])
    print(a[1])
    print(a[-1])

import numpy as np

a = np.array([
    [[1, 2], [3, 4], [5, 6]],
    [[5, 6], [7, 8], [9, 10]],
])

print(a[0, 0, 1])  # 2