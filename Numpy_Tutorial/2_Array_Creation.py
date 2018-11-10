import numpy as np

a = np.array([2, 3, 4])
print(a)
print('************************')

print(a.dtype)  
print('************************')

b = np.array([1.2, 3.5, 5.1])

print(b)
print('************************')

print(b.dtype) 
print('************************')

# wrong
# a = np.array(1, 2, 3, 4)
# right
# a = np.array([1, 2, 3, 4])

b = np.array([(1.5, 2, 3), (4, 5, 6)])

print(b)
print('************************')

c = np.array([[1,2], [3,4]], dtype=complex)

print(c)
print('************************')

print(np.zeros((3, 4)))
print('************************')

print(np.ones( (2,3,4), dtype=np.int16 ))
print('************************')

print(np.empty((2, 3)))
print('************************')

print(np.arange(10 , 30, 5))
print('************************')

print(np.arange(0, 2, 0.3))
print('************************')

from numpy import pi

print(np.linspace(0, 2, 9))
print('************************')

x = np.linspace(0, 2*pi, 100)
f = np.sin(x)

print(x)
print('************************')
print(f)
print('************************')

