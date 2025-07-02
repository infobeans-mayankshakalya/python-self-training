def cube(a):
    return a**3
print(cube(3))

lambda_cube = lambda a: a**3
print(lambda_cube(3))

lambda_even_odd = lambda a: "Even" if a % 2 == 0 else "Odd"
print(lambda_even_odd(4))
print(lambda_even_odd(5))