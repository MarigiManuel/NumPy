import os

file_path = os.path.join('aggregate_fncts', 'std.py')
with open(file_path, 'r') as file:
    import numpy as np

# Standard deviation measures how spread out the elements of an array is. 
# The more spread out elements is, the greater their standard deviation.
# Standard deviation is the square root of the variance.
# Syntax: numpy.std(a, axis=None, dtype=None, ddof=0, keepdims=<no value>)

# Calculate the standard deviation of all elements in a NumPy array
       
grades = np.array([88, 90, 95, 75, 83, 80])
std_grades = np.std(grades)

print(round(std_grades, 1))

# Calculate the standard deviation along a specified axis (for a 2D array):

diameters = np.array([[100, 230, 150, 300], [45, 200, 350, 600]])
result = np.std(diameters, axis = 0)
rounded_result = np.round(result, 1)          # Rounds off to 1 decimal place.

print(rounded_result)

# Calculate the standard deviation with specified degrees of freedom:

arr = np.array([1, 2, 3, 4, 5])
std_deviation_ddof1 = np.std(arr, ddof=1)  # Use ddof=1 for unbiased estimator
rounded_result = np.round(std_deviation_ddof1, 2)

print("Standard Deviation (ddof=1):", rounded_result)