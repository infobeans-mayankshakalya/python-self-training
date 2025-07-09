from numpy import *

a1 = arange(1,5)
a2 = a1.view()

print('a1', a1)
print('a2', a2)

a2[2] = 5

print('a1', a1)
print('a2', a2)

a3 = a1.copy()

print('a1', a1)
print('a2', a2)
print('a3', a3)

a3[2] = 10

print('a1', a1)
print('a2', a2)
print('a3', a3)
