a,b = [int(x) for x in input("Enter two numbers: ").split()]
try:
    assert a < b, "First number must be less than second number."
except AssertionError as e:
    print("Assertion Error:", e)
else:
    result = a / b
    print("Result:", result)
finally:
    print("Execution completed.")
