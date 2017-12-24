import numpy as np

arr = np.arange(0, 11)

print("arr      : ", arr)
print("arr[8]   : ", arr[8])
print("arr[0:5] : ", arr[0:5])

arr[0:5] = 100
print("arr : ", arr)

# again init arr
arr = np.arange(0, 11)
slice_of_arr = arr[0:6]
print("slice_of_arr : ", slice_of_arr)
# It is that make problem(affect original array)
slice_of_arr[:] = 99
print("arr : ", arr)
print("slice_of_arr : ", slice_of_arr)

# you should use this function
arr_copy = arr.copy()

# arr_2d pratice
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print("arr_2d : "	,    arr_2d)
print("arr_2d[1] : ",    arr_2d[1])
print("arr_2d[0] : ",    arr_2d[0])
print("arr_2d[1][0] : ", arr_2d[1][0])
print("arr_2d[:2, 1:] : ", arr_2d[:2, 1:])

arr_2d_10 = np.zeros((10, 10))
arr_length = arr_2d_10.shape[0]

for i in range(arr_length):
	arr_2d_10[i] = i

#print(arr_2d_10)
print(arr_2d_10[[2, 4, 6, 8]])
