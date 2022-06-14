# 1) Write a program to return a boolean value as a print statement if one number is greater than another.
#        E.g. If X is greater than Y return True otherwise return False

# a = int(input("a= "))
# b = int(input("b= "))
# if a > b:
#     print(f'a is greater than b {a} > {b}')
# else:
#     print(f'b is greater than a {b} > {a}')

# 2) Modify the previous program to return a string value as a print statement like:
# 	"10 is greater than 5" Or opposed "2 is less than 4"

# a = int(input("a= "))
# b = int(input("b= "))
# if a > b:
#     print(f'{a} is greater than {b}')
# else:
#     print(f'{a} is less than {b}')

# 3) Modify the previous program to cover the case to compare only positive numbers, zero is not included!
# in case one of the variables is zero return a string value as a print statement like:
# "One or both numbers are not positive, can't proceed with the comparison!"

a = int(input("a= "))
b = int(input("b= "))
if (a > 0) and (b > 0):
    if (a > b):
        print(f'{a} is greater than {b}')
    else:
        print(f'{b} is greater than {a}')
else:
    print("One or both numbers are not positive, can't proceed with the comparison!")
