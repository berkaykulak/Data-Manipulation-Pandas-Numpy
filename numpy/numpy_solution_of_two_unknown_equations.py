import numpy as np

a = np.array([[5,1], [1,3]])
b = np.array([12,10])

print(a)
print(b)

x = np.linalg.solve(a, b)
print(x)
