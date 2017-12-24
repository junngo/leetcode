import numpy as np

# list
my_list1 = [1, 2, 3, 4]
my_list2 = [11, 22, 33, 44]
my_lists = [my_list1, my_list2]

# array
my_array1 = np.array(my_list1)
my_array2 = np.array(my_lists)

print(my_array2)
print(my_array2.shape)
print(my_array2.dtype)

# if you wanted an array of all zeros
my_zeros_array = np.zeros(5)
# if you wanted an array of all one
my_ones_array = np.ones([5,5])
# if you wanted an array of empty
my_empty_array = np.empty(5)

print(np.arange(5))
print(np.arange(5, 50, 2))
