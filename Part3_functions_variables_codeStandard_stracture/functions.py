# x = input("What's your name? ")

# def function_name(x):
#     return (f" Hello {x}!")
#
# print((function_name("olya")))


###################################
# num = input("What's your number? ")
# num2 = input("what's your second number? ")
# def sum(x, y):
#     print(x + y)
# sum(5, 6)

###################################

name = input("What is your name? ")
num = int(input("what is your number? "))
while num not in int:
    print(f'Only digits are acceptable! Please enter your number: {num}')
def customer_number():
    global name
    global num
    print(f"Hello {name}, your current number is {num}")

customer_number()
