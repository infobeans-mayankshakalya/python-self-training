s={10,20,13.4,'mayank',10}
print(s)
print(type(s))
s.update([33,67])
print(s)
# print(s.index(33)) not applicable for sets
s.add(100)
print(s)
s.remove(10)
print(s)
s.discard(20)
print(s)
s.pop()
print(s)
s.clear()
print(s)
f=frozenset(s)
print(f)
print(type(f))
# f.add(200)  # frozensets are immutable, so this will raise an

# assignement
countries = {'India', 'USA', 'Canada', 'Australia', 'Germany'}
print(countries)
countries.add('Japan')
print(countries)
countries.update(['France', 'Italy'])
print(countries)
countries.pop()
print(countries)