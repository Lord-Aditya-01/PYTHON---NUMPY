import numpy as np

arr = np.array([1.5 , 2.6 , 3.0])
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr)
print(int_arr.dtype)
