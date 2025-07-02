a=10
b=10
print(a is b)  # True, because both refer to the same immutable integer object
print(id(a), id(b))  # Different IDs, confirming they are different objects
b = 20
print(a is b)  # False, because b now refers to a different integer object 
print(id(a), id(b))  # Different IDs, confirming they are different objects


a0 = [10, 20]
b0 = [10, 20]
print(a0 is b0)  # False, because lists are mutable and a new object is created
print(id(a0), id(b0))  # Different IDs, confirming they are different objects

a=10
b=10
a1 = [10, 20]
b1 = [10, 20]
print(a1[0] is b1[0])  # True
print(id(a1[0]), id(b1[0]))  # Same IDs, confirming they are same objects

print(a1[0] is a)  # True
print(id(a1[0]), id(a))  # Same IDs, confirming they are same objects