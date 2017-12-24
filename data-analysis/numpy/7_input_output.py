import numpy as np

arr = np.arange(5)
np.save('myarray', arr)
arr = np.arange(10)
np.load('myarray.npy')

arr1 = np.load('myarray.npy')
arr2 = arr

#save zip file
np.savez('ziparray.npz', x=arr1, y=arr2)

archive_array = np.load('ziparray.npz')

print(archive_array['x'])
print(archive_array['y'])

#save txt file
arr = np.array([[1,2,3],[4,5,6]])
np.savetxt('mytextarray.txt', arr, delimiter=',')
arr = np.loadtxt('mytextarray.txt', delimiter=',')
