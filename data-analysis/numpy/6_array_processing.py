import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

points = np.arange(-5, 5, 0.01)
dx, dy = np.meshgrid(points, points)
z = (np.sin(dx) + np.sin(dy))

plt.imshow(z)
plt.colorbar()
plt.title('Plot for sin(x)+sin(y)')
#plt.show()

#numpy where
A = np.array([1, 2, 3, 4])
B = np.array([100, 200, 300, 400])
condition = np.array([True, True, False, False])
answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A, B, condition)]
# answer = answer2
answer2 = np.where(condition, A, B)

#random array
arr = randn(5, 5)

#where example
np.where(arr<0, 0, arr)

# module example
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr.sum() 	# 45
arr.sum(0)	# [12,15,18]
arr.mean()	# 5.0
arr.std()	# 2.5819888974716112
arr.var()	# 6.66666666666667

bool_arr = np.array([True, False, True])
bool_arr.any()	# True
bool_arr.all()	# False

#sort
arr = randn(5)
arr.sort()	# from least to greatest

countries = np.array(['France', 'Germany', 'USA', 'Russia', 'USA', 'Mexico', 'Germany'])
np.unique(countries)
np.in1d(['France', 'USA', 'Sweden'], countries)
