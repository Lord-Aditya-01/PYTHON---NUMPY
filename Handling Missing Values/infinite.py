# np.isinf()  10^10000
# 1/10

import numpy as np

arr = np.array([1,2,3,np.inf,5,np.inf])

print(np.isinf(arr))