import numpy as np

arr = np.arange(50).reshape((10, 5))

print(arr)
print(arr.T)

arr_dot = np.dot(arr.T, arr)
print(arr_dot)

arr3d = np.arange(50).reshape((5, 5, 2))
print(arr3d)
print(arr3d.transpose((1, 0, 2)))

arr = np.array([[1,2,3]])
print(arr)
print(arr.swapaxes(0, 1))
