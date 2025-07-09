from numpy import *

a1 = array([10, 30, 50,90])
a2 = array([20, 40,60,80])

print(a1>a2)
print(a1<a2)
print(a1>=a2)

print(any(a1>a2))
print(any(a1<a2))
print(all(a1>a2))
print(all(a1<a2))

print(where(a1<a2,a1,a2))
print(where(a1>a2,a1,a2))