lst={10,25,55,23,50,100,200,300,400,500}
even_numbers = filter(lambda x: x%2==0, lst)  # This will return a filter object
under_100 = filter(lambda x: x < 100, lst)  # This will return a filter object
for each in even_numbers:
    print(each, end=' ')
print()
for each in under_100:
    print(each, end=' ')
print()

intersection = filter(lambda x: x in even_numbers, under_100)  # This will return a filter object
print("Intersection of even numbers and under 100:")
for each in intersection:
    print(each, end=' ')
print()