# array has a fixed size so if you have to add a element in array another array is created

"""
np.insert(array, index, value, axis=None)
axis = 0, row-wise insertion
axis = 1, column-wise insertion

"""

import numpy as np

arr = np.array([10,20,30,40,50,60]) 

new_arr = np.insert(arr,2,100,0)
print(new_arr)