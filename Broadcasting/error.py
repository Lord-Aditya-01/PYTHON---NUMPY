import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([1,2,3,4,5,6])
# result = arr1 + arr2
# .reshape
new_arr = np.reshape(arr2,(2, 3))
result = arr1 + new_arr
print(result)
