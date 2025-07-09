from numpy import *

a1 = array([1,2,3,4,5,6,7])
a2 = array([[1,2,3,4],[5,6,7,8]])
a3 = array([
                [
                    [1,2,'c'],
                    [3,4,'d']
                ],
                [
                    [5,6,'e'],
                    [2,7,8]
                ]
            ])

print(a1,a2,a3)
print(a1.ndim,a2.ndim,a3.ndim)

