import numpy as np
a = np.random.randint(10, size = 10)
print(a)
print(a[0])
print(a[-1])
a[0] = 100
print(a)
m = np.random.randint(10, size = (3,5))

print(m)
print(m[0,0])
print(m[1,1])
print(m[1, 4])
m[1, 4] = 99
print(m)
m[1,4] = 2.2
print(m)