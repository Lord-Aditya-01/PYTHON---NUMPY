import numpy as np
"""
slicing -> 
arr[start:stop:step]
arr[start:End] , start to end -1

"""

arr = np.array([10,20,30,40,50])

print(arr[1:4])
print(arr[:3])
print(arr[1:])
print(arr[-3:-1])
print(arr[::2])
print(arr[::-1])