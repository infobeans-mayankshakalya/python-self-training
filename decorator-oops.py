import math

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return f"Salary is: {self._salary}"
    
    @salary.setter
    def salary(self, salary):
        self._salary = math.floor(salary)
e = Employee('Mayank', 500000.35)
print(e.name)
print(e.salary)
e.salary = 55555.85
print(e.salary)