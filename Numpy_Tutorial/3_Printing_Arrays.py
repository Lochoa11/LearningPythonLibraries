import numpy as np

a = np.arange(6)

print(a)
print('***********************')

b = np.arange(12).reshape(4,3)

print(b)
print('***********************')

c = np.arange(24).reshape(2, 3, 4)
print(c)
print('***********************')

print(np.arange(10000))
print('***********************')

print(np.arange(10000).reshape(100, 100))
print('***********************')

np.set_printoptions(threshold=np.nan)
print(np.arange(10000).reshape(100, 100))

