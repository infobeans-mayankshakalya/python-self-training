try:
    a,b = [int (x) for x in input("Enter two numbers: ").split()]
    result = a / b
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.")
    print("Exception message:", e)
except ValueError as e:
    print("Error: Invalid input. Please enter valid integers.")
    print("Exception message:", e)
else:
    print("Result:", result)
finally:
    print("Execution completed.")