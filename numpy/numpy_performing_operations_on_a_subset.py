import numpy as np
a = np.random.randint(10, size = (5, 5))
print(a)

alt_a = a[0:3, 0:2]
print(alt_a)

alt_a[0,0] = 99999
alt_a[1,1] = 888

print(alt_a)
print(a)

m = np.random.randint(10, size = (5, 5))
print(m)

alt_b = m[0:3, 0:2].copy()
alt_b[0,0] = 9999

print(alt_b)
print(m)











