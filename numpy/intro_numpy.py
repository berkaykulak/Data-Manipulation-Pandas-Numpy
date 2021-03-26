import numpy as np

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
  ab.append(a[i]*b[i])

print(ab)

a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

print(a * b)