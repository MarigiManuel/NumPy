import os

file_path = os.path.join('aggregate_fncts', 'sum.py')
with open(file_path, 'r') as file:
    import numpy as np

a = np.array([1, 2, 3])
total = np.sum(a)
print(total)

# Sum of 2-D array

b = np.array([[1, 2, 3],
              [4, 5, 6]
            ])
x = np.sum(b)

print(x)

# The sum() function also accepts the axis argument that allows you to return the sum of elements of an axis

numbers = np.array([[2, 3, 4],
                     [5, 6, 7],
                     [8, 9, 10]
                     ])
total = np.sum(numbers)
x = np.sum(numbers, axis = 0)
y = np.sum(numbers, axis = -1)

print(total)
print(x)
print(y)


# Summary:
# Use the sum() function to get the sum of all elements of an array.
# Use the axis argument to specify the axis that you want to sum u