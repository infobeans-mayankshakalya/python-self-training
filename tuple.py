tpl=(1,2,3,4,5,6,7,8,9,10,'mayank',True, 3.14, 0xFF, 0b1010, 0o77, 3+5j)
print(tpl)
print(tpl[13])
print(tpl[3:6])
print(tpl*2)
print(tpl[::-1])
# tpl.append(200)  # Tuples are immutable, so this will raise an error
# print(tpl)
# tpl.insert(2, 150)  # Tuples are immutable, so this will raise an error
# print(tpl)
# tpl.remove('mayank')  # Tuples are immutable, so this will raise an error
# tpl.remove(True)  # Tuples are immutable, so this will raise an error
# tpl.remove(3.14)  # Tuples are immutable, so this will raise  an error
# tpl.remove(0xFF)  # Tuples are immutable, so this will raise an error
# tpl.remove(0b1010)  # Tuples are immutable, so this will raise an error
# tpl.remove(0o77)  # Tuples are immutable, so this will raise an error
# tpl.remove(3+5j)  # Tuples are immutable, so this will raise an error
# print(tpl)
# del(tpl[3])  # Tuples are immutable, so this will raise an error
# print(tpl)
# tpl.sort()  # Tuples are immutable, so this will raise an error
# print(tpl)
# tpl.sort(reverse=True)  # Tuples are immutable, so this will raise an error
# print(tpl)

#assignement
countries = (1,2,4,'india',True)
print(countries[0],countries[2])
print(countries.index('india'))
print(len(countries))
print(4 in countries)