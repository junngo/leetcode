import numpy as np
import webbrowser

arr = np.arange(11)

print(np.sqrt(arr))
print(np.exp(arr))

A = np.random.randn(10)
B = np.random.randn(10)

# Binary Functions
np.add(A, B)

# Maximum between array
print(np.maximum(A, B))

website = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'
webbrowser.open(website)
