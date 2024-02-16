# Introduction to the numpy any() function
import os

file_path = os.path.join('aggregate_fncts', 'any.py')
with open(file_path, 'r') as file:
    import numpy as np

# The numpy any() function returns True if any element in an array (or along a given axis) evaluates to True.
#Typically, the input array contains numbers. In the boolean context, all non-zero numbers evaluate to True while zero evaluates to False. 
# Therefore, the any() function returns True if any number in the array is nonzero or False if all numbers are zero.

# Using numpy any() function on 1-D array examples

result = np.any([0, 1, 2, 3])
print(result)            # True

result = np.any([0, 0])
print(result)            # False

# Using numpy any() function with a multidimensional array example
a = np.array([[0, 1], [2, 3]])
result = np.any(a)        # True
print(result)

a = np.array([[0, 0], [2, 3]])
result = np.any(a)         # True
print(result)

a = np.array([[0, 1], [2, 3]])
result = np.any(a, axis = 0)   # [True True]
print(result)

a = np.array([[0, 1], [0, 3]])
result = np.any(a, axis = 0)               # [False True]
print(result)

a = np.array([[0, 1], [0, 3]])
result = np.any(a, axis = 1)               # [True True]
print(result)

a = np.array([[0, 1], [0, 0]])
result = np.any(a, axis = 0)               # [False True]
print(result)