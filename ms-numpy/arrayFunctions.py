from numpy import *

a1 = arange(12)

print(a1)
a2 = reshape(a1,(2,6))
print(a2)

a3 = reshape(a1, (2,2,3))
print(a3)

a4 = a3.flatten()
print(a4)

a5 = eye(4)
print(a5)