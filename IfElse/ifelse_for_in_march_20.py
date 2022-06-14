# Write a program that compares the password and it's confirmation.
# If they match, then the program displays: "Accepted", otherwise: "Declined"

# password = int(input("Enter your password "))
# print(type(password))
# confirmPassword = int(input("Confirm password "))
# print(type(confirmPassword))
# if password == confirmPassword:
#     print("Accepted")
# else:
#     print("Declined")


# Write a program that determines if a number is even or odd
#
# a = int(input("Enter you number"))
#
# if a%2 == 0:
#     print(f'The number {a} is even')
# else:
#     print(f'the number {a} is odd')
#
# # a%2 means if we devide number a by 2 and we don't have any float number it means 0 (even)
# a%2 = 0, 2/2 =1.0, or 3/2 =1.5'



""""
Write a program that determines whether a user is allowed to access an Internet resource or not.
The program should display the text "Access granted" if the age is at least 18, and "Access denied" otherwise
"""
# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print(f'Your age is {age}. Access granted')
# else:
#     print(f'Your age is {age}. Access is denied')


"""Write a program to calculate and evaluate a person's body mass index (BMI)
BMI = mass, (kg) / height (m) * height (m)
The program should output "Optimal Weight" if the BMI is between
if 18.5 and 25(inclusive):
"Underweight" if BMI is less than 18.5 and "Overweight" if BMI is greater than 25."""
# #1
# kg = float(input("Enter your weight: "))
# height = float(input("Enter you height in meters: "))
# BMI = kg / (height * height)
# if BMI < 18.5:
#     print(f'Your mass is {BMI}. Underweight')
# elif BMI >= 18.5 and BMI <= 25:
#     print(f'Your mass is {BMI}. Optimal Weight')
# else:
#     print(f'Your mass is {BMI}. Overweight')
#
# #2
# kg = float(input("Enter your weight: "))
# height = float(input("Enter you height in meters: "))
# BMI = kg / height ** 2
# if BMI < 18.5:
#     print(f'Your mass is {BMI}. Underweight')
# elif BMI >= 18.5 and BMI <= 25:
#     print(f'Your mass is {BMI}. Optimal Weight')
# elif BMI > 25:
#     print(f'Your mass is {BMI}. Overweight')

"""
Write a program that takes integer x and determines if the given number
belongs to the specified range (-1, 17), not including the boundaries
"""
# a = int(input("Enter your number: "))
# if a < 17 and a > -1:
#     print("Correct")
# else:
#     print("Not correct")

"""
Write a program that takes an integer x and determines if the given # belongs to the specified range(∞, -3)
and then (7, ∞), including the boundaries
"""

# x = int(input("Enter the number: "))
# if x <= -3 or x >= 7:
#     print(f'{x} is correct')
# else:
#     print(f'{x} is not correct')

"""
Write a program that takes an integer x and determines if the given number belongs to the specified range
(-30, -2) and then (7, 25), left boundaries are not included and right ones are included
"""
#1
# x = int(input("Enter number: "))
# if x > -30 and x <= -2:
#     print(f'{x} belongs to (-30, -2)')
# elif x > 7 and x <= 25:
#     print(f'{x} belongs to (7, 25)')
# else:
#     print(f"{x} don't belongs to (7, 25) and (-30, -2)")

#2
# x = int(input("Enter number: "))
# if (-30 < x <= -2) or (7 < x <= 25):
#     print("Included")
# else:
#     print("Not included")
#
# #3
# x = int(input("Enter number: "))
# if (x > -30 and  x <= -2) or (x > 7 and x <= 25):
#     print("Included")
# else:
#     print("Not included")


"""
Write a program that takes three positive numbers and determines if there exists a triangle with such sides
"""
#
# a = abs(int(input("Enter the lenght of 1st side: ")))
# b = abs(int(input("Enter the lenght of 2nd side: ")))
# c = abs(int(input("Enter the lenght of 3rd side: ")))
#
# if a == b == c :
#     print("Triangle")
# else:
#     print("Not triangle")

"""
Write a program that takes three positive numbers and determines the type of triangle whose side lenght
The program should display test on screen - a kind of triangle ("Equilateral , "Isosceles" or "Scales")
"""
# a = abs(int(input("First side: ")))
# b = abs(int(input("Second side: ")))
# c = abs(int(input("Third side: ")))
#
# if a == b == c :
#     print("The triangle is Equilateral")
# elif a == b or a == c or c == b:
#     print("The triangle is Isosceles")
# else:
#     print("The triangle is Scales")


"""
Write a program where the function more_than_five(lst) receives a list of integers. The result of the function 
should be a new list, which contains only those numbers that are greater than 5 module 
"""
# (lst) this is varable that contains list of some numbers
# lst = [7, 8, 9, -6]

def more_than_five(lst):
    new_list = []
    for i in lst:
        if abs(i) > 5:
            new_list.append(abs(i))
            #append put element into the end of the list
    # print(new_list)
    return new_list
# заверщаем функцию , если ее не указывать, она не завершится

print(more_than_five([-11, 4, 2, 90, 400, 0, -5]))
print(more_than_five([-2, 2, 3, 4, 0, -1]))
print(more_than_five([78, -900, 2, 41, 0]))