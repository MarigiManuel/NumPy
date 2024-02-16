import os

file_path = os.path.join('aggregate_fncts', 'prod.py')
with open(file_path, 'r') as file:
    import numpy as np

# Using the numpy prod() function with 1-D array example
    
a = np.arange(1, 5)
result = np.prod(a)

print(a)
print('Result:', result)

# Using the numpy prod() function with multidimensional array examples

result = np.prod([[1, 2, 3], 
                  [4, 5, 6]
                  ])
print(result)

# The following uses the prod() to calculate the product of numbers on axis 0:
result = np.prod([
    [1, 2],
    [3, 4]
], axis=0)            # Product for axis 0

print(f'result={result}')

###########
result = np.prod([
    [1, 2],
    [3, 4]
], axis=1)             # Product for axis 1

print(f'result={result}')

# Selecting numbers to include in the product

result = np.prod([0, 3, 7], where =[False, True, True])
print(result)

#########

a = np.array([np.nan, 3, 4])
result = np.prod(a, where=[False, True, True])
print(result)

# Special cases
# Note that if you pass an array of integers to the prod() function that causes an overflow, the prod() won’t raise the error. For example:
result = np.prod(np.arange(1, 100))
print(f'result={result}')

# The prod() function returns 1 if the array is empty. For example:

a = np.array([])
result = np.prod(a)

print(result)