
class InvalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg

try: 
    password = input("Enter your password: ")
    if len(password) < 8:
        raise InvalidPasswordException("Password must be at least 8 characters long.")
except InvalidPasswordException as e:
    print("Invalid password:", e.msg)
else:
    print("Password is valid.")
finally:
    print("Password validation completed.")