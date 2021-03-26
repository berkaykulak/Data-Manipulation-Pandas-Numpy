import numpy as np

np.arange(1,10)
np.arange(1,10).reshape((3,3))
a = np.arange(1,10)
print(a)
print(a.ndim)

b = a.reshape((1,9))
print(b.ndim)
