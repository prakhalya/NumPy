import numpy as np

arr = np.array([6, 99, 10, 9])

x = np.searchsorted(arr, 7)

print(x)
