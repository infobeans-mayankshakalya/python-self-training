import sys
# print(sys.argv)
# sys.exit()
_a,bankingOption, amount = sys.argv
balance = 1000
match bankingOption:
    case '1':
        print(f"Your current balance is {balance}")
    case '2':
        depositAmount = int(sys.argv[2])
        balance += depositAmount
        print(f"Your new balance after deposit is {balance}")
    case '3':
        withdrawAmount = int(sys.argv[2])
        if withdrawAmount > balance:
            print("Insufficient balance")
        else:
            balance -= withdrawAmount
            print(f"Your new balance after withdrawal is {balance}")
    case '4':
        print("Thank you for using our banking service. Goodbye!")
    case _:
        print("Invalid option. Please try again.")