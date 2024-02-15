import os

file_path = os.path.join('Array_Indexing&Slicing', 'fancy.py')
with open(file_path, 'r') as file:
    import numpy as np

# Fancy indexing allows you to index an array using another array, a list, or a sequence of integers.
    
a = np.arange(2, 10)

print(a)

f = np.array([2, 4, 6])

print(a[f])