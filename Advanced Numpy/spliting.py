# """

# np.split() -> splits equally
# np.hplit() -> splits horizontally
# np.vplit() -> splits vertically

# """
# import numpy as np

# arr = np.array([10,20,30,40,50,60]) 
# # arr1 = np.array([1,2,3]) 
# # arr2 = np.array([4,5,6])

# print(np.split(arr,2))
# print(np.hsplit(arr,2))
# import numpy as np

# a = np.array([list(map(int, input().split()))])
# print(a)
# arr = np.split(a,3)
# print(arr)

# import numpy as np
# matrix_a = np.array([list(map(int, input().split())) for i in range(3)])
# print(matrix_a)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
a= int(input())
print(np.where(arr==a)[0])