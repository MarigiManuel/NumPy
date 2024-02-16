import os

file_path = os.path.join('aggregate_fncts', 'var.py')
with open(file_path, 'r') as file:
    import numpy as np


# Use the numpy var() function to calculate the variance of elements in an array.
# Variance measures the dispersion or spread of a dataset. 
# It quantifies how much the values in a dataset deviate from the mean.
# Syntax: numpy.var(a, axis=None, dtype=None, ddof=0, keepdims=<no value>)

# Calculate the variance of all elements in a NumPy array:
    
arr = np.array([1, 2, 3, 4, 5])
variance = np.var(arr)

print("Variance:", variance)

# Calculate the variance along a specified axis (for a 2D array):

arr = np.array([[1, 2, 3], [4, 5, 6]])
# Calculate variance along the rows (axis=0)
variance_row = np.var(arr, axis=0)
print("Variance along rows:", variance_row)

# Calculate variance along the columns (axis=1)
variance_col = np.var(arr, axis=1)
print("Variance along columns:", variance_col)

# Calculate the variance with specified degrees of freedom:

arr = np.array([1, 2, 3, 4, 5])
variance_ddof1 = np.var(arr, ddof=1)  # Use ddof=1 for unbiased estimator

print("Variance (ddof=1):", variance_ddof1)