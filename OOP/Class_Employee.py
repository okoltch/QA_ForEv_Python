class Employee:
    """Common base class for all employees"""
    empCount = 0        #will count our employees

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    @staticmethod
    def displayCount():
        print("Total Employee %d" % Employee.empCount)
        #%d is the format specifier used to print integers or numbers

    def displayEmployee(self):
        print(f"Name: {self.name}. Salary: {self.salary}")

"""This will create first object of Employee class"""
emp1 = Employee("Zara", 2000)
"""This will create second object of Employee class"""
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()

emp2.displayEmployee()
# print("Total Employee %d" % Employee.empCount)
Employee.displayCount()