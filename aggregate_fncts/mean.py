import os

file_path = os.path.join('aggregate_fncts', 'mean.py')
with open(file_path, 'r') as file:
    import numpy as np

# mean() syntax
# numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>, *, where=<no value>)
    
a = np.array([2, 4, 6])
average = np.mean(a)

print(average)

# Using NumPy mean() function on 2-D array example:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
average = np.mean(a, axis=0)
print(average)

# Specifying a where argument:
x = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]
              ])
average = np.mean(x)
print(average)

y = np.mean(x, where = [[False], [True], [True]])
print(y)