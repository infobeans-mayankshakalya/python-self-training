from pandas import *

reviews = Series([1.2,2.5,4.7,5.1,6.3,7])
print(reviews)
print(reviews.describe())

print(reviews[0])

print(reviews.count)
print(reviews.min())
print(reviews.max())
print(reviews.mean())
print(reviews.std())


reviews = Series([1.2,2.5,4.7,5.1,6.3,7], index=['python', 'java', 'c++', 1, 2, 4,])
print(reviews)
print(reviews[1])
print(reviews.java)
print(reviews.values)
print(reviews.keys)

courses = Series(['java', 'python', 'AWS'])
print(courses)
print(courses.str.upper())
print(courses.str.lower())
print(courses.str.contains('y'))
