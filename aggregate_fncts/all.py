# Introduction to the numpy all() function
import os

file_path = os.path.join('aggregate_fncts', 'all.py')
with open(file_path, 'r') as file:
    import numpy as np

# The numpy all() function returns True if all elements in an array (or along a given axis) evaluate to True.
# If the input array contains all numbers, the all() function returns True if all numbers are nonzero or False if least one number is zero. 
# The reason is that all non-zero numbers evaluate to True while zero evaluates to False.

# Using numpy all() function on 1-D array examples
result = np.all([0, 1, 2, 3])
print(result)     # False

result = np.all([1, 2, 3])
print(result)       # True

result = np.all([-1, 2, 3])
print(result)        # True

# Using the numpy all() function with a multidimensional array example

a = np.array([
    [0, 1],
    [2, 3]
])
result = np.all(a, axis=0)

print(result)     # [False True]

a = np.array([
    [0, 1],
    [2, 3]
])
result = np.all(a, axis=1)  # [False True]
print(result)