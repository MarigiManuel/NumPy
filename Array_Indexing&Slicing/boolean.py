import os

file_path = os.path.join('Array_Indexing&Slicing', 'boolean.py')
with open(file_path, 'r') as file:
    import numpy as np
"""
# Example 1
    
# First, create an array that has 9 numbers from 1 to 9 using the arange() function.
a = np.arange(3, 8)
print(a)

# Second, create a boolean array
b = a > 5
print(b)

# Third, use the array b as the index of array a and assign the result to the variable c
c = a[b]
print(c)

# Example 2

n = np.array([2, 4, 6, 1])
d = np.array([False, True, True, False])
a = n[d]

print(a)
"""
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# make a copy
b = a[0:, 0:2].copy()
print(b)

b[0, 0] = 0
print(b)

print(a)