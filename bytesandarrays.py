lst=[20,252]
print(lst)
b=bytes(lst)
print(b)
print(type(b))
print(b[0])

b1=bytearray(lst)
print(b1)
print(type(b1))
b1[0]=100
print(b1)