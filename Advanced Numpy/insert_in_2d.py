import numpy as np

arr = np.array([[1,2],[33,4]]) 

new_arr = np.insert(arr, 1, [5,6], axis=0)
print(new_arr)

"""

axis = none -> makes flatten
axis = 1 -> arranges column-wise
axis = 0 -> arranges row-wise

"""