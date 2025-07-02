def m1():
    a=10

# print(a) # This will raise an error because 'a' is not defined in this scope
a = None  # Assigning None to 'a'
print(type(a))
print(m1())