import os

file_path = os.path.join('Array_Indexing&Slicing', 'slicing.py')
with open(file_path, 'r') as file:
    import numpy as np

# Numpy array slicing on on-dimensional arrays  
a = np.arange(0, 10)

print('a=', a)
print('a[2:5]=', a[2:5])
print('a[:]=', a[:])
print('a[0:-1]=', a[0:-1])
print('a[0:6]=', a[0:6])
print('a[7:]=', a[7:])
print('a[5:-1]=', a[5:-1])
print('a[0:5:2]=', a[0:5:2])
print('a[::-1]=', a[::-1])

# Numpy array slicing on multidimensional arrays

# In this example below, array a is a 2-D array. In the expression a[0:2, :]:
# First, the 0:2 selects the element at index 0 and 1, not 2 that returns:
# Then, the : select all elements. Therefore the whole expression returns.

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[0:2, :])


# In the example below, First, 1: selects the elements starting at index 1 to the last element of the first axis (or row).
# Second, 1: selects the elements starting at index 1 to the last elements of the second axis (or column).

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(a[1:, 1:])