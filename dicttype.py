dict1={1:"john", 2:"doe", 3:"jane", 4:"smith", 5:"alice", 6: 5, "mayank": 10, "python": 20.54, "is": True, "awesome": "I am the best"}
print(dict1)
print(dict1.values())
print(dict1.keys())
print(dict1.items())
for key, value in dict1.items():
    print(f"Key: {key}, Value: {value}")

del dict1[1]
print(dict1)

# assignment
dict2 = {'name': 'Alice', 'age': 30, 'major': 'Computer Science'}
print(dict2['name'],dict2['age'])
dict2['email'] = 'alice.wonderland@test.com'
print(dict2)
dict2['age'] = 31
print(dict2)
dict2.pop('major')
print(dict2)