'''
reshaping does not create a copy it creates a view
reshape(rows,column) specify new shape
if dimensions match
it affects original array
'''

import numpy as np

arr = np.array([10,20,30,40,50,60])
reshape = arr.reshape(2,3)
print(reshape)