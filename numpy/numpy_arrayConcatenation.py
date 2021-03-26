import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.concatenate([x, y]))

z = np.array([7,8,9])

print(np.concatenate([x, y, z]))

a = np.array([[1,2,3],
              [4,5,6]])


print(np.concatenate([a,a]))
print(np.concatenate([a,a], axis = 1))

















