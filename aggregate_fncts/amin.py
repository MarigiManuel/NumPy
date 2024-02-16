# NumPy amin()

import os

file_path = os.path.join('aggregate_fncts', 'amin.py')
with open(file_path, 'r') as file:
    import numpy as np

# The amin() function returns the minimum element of an array or minimum element along an axis.
# Syntax: numpy.amin(a, axis=None, out=None, keepdims=<no value>, initial=<no value>, where=<no value>)
# The amin() function is equivalent to the min() method of the ndarray object:
    
# sing numpy amin() function on 1-D array example

a = np.arange(3, 9)
result = np.amin(a)

print(a)
print(result)

# Using numpy amin() function on multidimensional array examples

b = np.array([[2, 3, 6], [7, 3, 10]])
result = np.amin(b)
zero_axis = np.amin(b, axis = 0)
one_axis = np.amin(b, axis = 1)

print(result)
print(zero_axis)
print(one_axis)


# While the amin() returns the minimum element, 
# The amax() function returns the maximum element of an array or maximum element along an axis.