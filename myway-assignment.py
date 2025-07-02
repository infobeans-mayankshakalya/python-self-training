toppings=['tomato','onion','cheese','pepperoni','mushroom']
print("Welcome to the Pizza Shop!")
print("Available toppings:")
for topping in toppings:
    print(f"- {topping}")
print("You can choose any three toppings for your pizza.")
# Prompt the user to enter their toppings
topping = input("Enter any three topping(sep with comma): ").split(',').strip()
# Check if the user has entered three toppings
if len(topping) != 3:
    print("Please enter exactly three toppings.")
    topping = input("Enter any three topping(sep with comma): ").split(',').strip()
else:
    qty = int(input("Please enter the quantity:"))
    if(qty<=0):
        print("Please enter a valid quantity greater than 0")
        qty = int(input("Please enter the quantity:"))
    else:
        print(your_pizza := f"Your pizza with {topping[0]}, {topping[1]}, and {topping[2]} is ready! Quantity: {qty}")
        print("your bill is:", qty * 5, "dollars")