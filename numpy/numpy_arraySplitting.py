import numpy as np

x = np.array([1,2,3,99,99,3,2,1])

print(np.split(x, [3,5]))

a,b,c = np.split(x, [3,5])
print(a)
print(b)
print(c)

m = np.arange(16).reshape(4,4)

print(np.vsplit(m, [2]))

ust, alt = np.vsplit(m, [2])
print(ust)
print(alt)

print(np.hsplit(m, [2]))

sag, sol = np.hsplit(m, [2])

print(sag)
print(sol)






