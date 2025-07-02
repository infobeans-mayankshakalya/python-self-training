from functools import reduce
sum = lambda x, y: x + y
lst = [8, 9, 1991]
# def split_digits(number):
#     return [int(d) for d in str(number)]


# lst = filter( lambda x: [(int(x) for x in str(x))], [8, 9, 1991])
# lst = list(lst)
# print(lst)

result = str(reduce( sum, lst))
print(result)

# print(split_digits(lst[2]))