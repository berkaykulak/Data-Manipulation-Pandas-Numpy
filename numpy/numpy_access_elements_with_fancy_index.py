import numpy as np
v = np.arange(0, 30, 3)
print(v)

print(v[1])
print(v[3])
print(v[5])
print([v[1], v[3], v[5]])

al_getir = [1,3,5]
print(v)
print(v[al_getir])

m = np.arange(9).reshape((3,3))
print(m)
satir = np.array([0,1])
sutun = np.array([1,2])

print(m[satir, sutun])
print(m)
print(m[0, [1,2]])
print(m[0:, [1,2]])




