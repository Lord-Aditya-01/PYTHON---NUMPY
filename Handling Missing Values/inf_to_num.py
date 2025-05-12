import numpy as np

arr = np.array([1,2,3,np.inf,5,np.inf])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr,posinf=100)
print(cleaned_arr)