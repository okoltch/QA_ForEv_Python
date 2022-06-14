
a = input("Enter a number: ")
b = input("Enter one more number: ")
operation = input("Enter operation: +, -, * or / ")
while not a.isdigit():
    print("Only digits are accepted")
    a = input("Enter the first number: ")
while not b.isdigit():
    print("Only digits are accepted")
    b = input("Enter the second numer: ")
while operation not in ["+", "-", "*", "/"]:
          print("Only digits are accepted")

a = int(a)
b = int(b)
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    if a == 0:
        print("No division by zero!")
    elif b == 0:
        print("No division by zero!")
    else:
        print(a / b)

else:
    print("Invalid operation")
