# a = 8
# b = 9
#
#
#
# if b > a:
#     print('b is greater than a')
# elif a == b:
#     print('a and b are equal')
# else:
# #     print('a is greater that b')
# print("-" * 12)
# print(("|" + " " * 10 + "|"),("|" + " " * 10 + "|"),("|" + " " * 10 + "|"), sep="\n")
# print("-" * 12)
#
# name  = input("what is your name?")
# print(type(name))
# print("Hello, ", name)
# print(int(input()) + int(input()) + int(input()))
#
# a = int(input('Input first value'))
# b = int(input('Input second value'))
# c = int(input('Input third value'))
# d = a + b + c
# print(d)

# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.
# На вход программе подается одно целое число – длина ребра.
# Примечание. Объём куба и площадь полной поверхности можно вычислить по формулам V = a^3,  S = 6a^2

# rib = int(input())
# V = rib ** 3
# S = 6 * rib **2
# print(f"Volume: {V}")
# print(f"Square: {S}")

# Напишите программу вычисления значения функции f(a, \, b) = 3(a + b)^3 + 275b^2 - 127a - 41 по введеным целым значениям aa и bb.
#
# a = int(input("Input value for 'a': "))
# b = int(input("Input value for 'b': "))
# c = 3 * (a + b) ** 3 + (275 * b) ** 2 - 127 * a
# f = c
# print(f'The result is {c}')

# Напишите программу, которая считывает целое число, после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

# a = int(input())
#
# print(f'The next value of {a} a will be {a + 1}')
# print(f'The previous value of {a} a will be {a - 1}')

# Напишите программу, которая считает стоимость трех компьютеров, состоящих из монитора, системного блока, клавиатуры и мыши.
# На вход программе подаётся четыре целых числа, каждое на отдельной строке. В первой строке — стоимость монитора,
# во второй строке — стоимость системного блока, в третьей строке — стоимость клавиатуры и в четвертой строке — стоимость мыши.

# a = int(input("The cost of screen is : "))
# b = int(input("The cost of  system operator is : "))
# c = int(input("The cost of keyboard is : "))
# d = int(input("The cost of mouse is : "))
# e = (a + b + c + d) * 3
# print(f"The cost of 3 computers are: {e}")

# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.
#
# a = int(input())
# b = int(input())
# sum = (a + b)
# difference = (a - b)
# multiple = (a * b)
# print((f'The sum of two values is {sum}'),
# (f'The difference between two values is {difference}'),
# (f'The multiple value of two numbers is {multiple}'), sep="\n")
# or other option
# a = int(input())
# b = int(input())
# print(f'{a} + {b} =', a + b)
# print(f'{a} - {b} =', a - b)
# print(f'{a} * {b} =', a * b)
# print(f'{a} / {b} =', a / b)

# Напишите программу, которая считывает целое положительное число xx и выводит на экран последовательность
# чисел x, \, 2x, \, 3x,\,4xx,2x,3x,4x и 5x5x, разделённых тремя черточками.
# # TO DO
# x = int(input())

# Напишите программу, которая находит полное число метров по заданному числу сантиметров.
# cm = int(input())
# m = cm//100
# print(f"The value of meters are: {m}")

#Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной
# по #щелчку пальцев. При этом если население Вселенной является нечетным числом,
# то титан проявит милосердие и округлит #количество выживших в большую сторону.
# Помогите Мстителям подсчитать количество выживших.

a = abs(int(input("population: ")))
survivors = a // 2 + a % 2
whole = a // 2
rest = a % 2
print(f'Survived people is going to be {survivors}')
print(whole)
print(rest)

# a = int(input("population"))
# if a == :
#     print(a // 2 + a % 2)
# else:
#     print(a // 2 )
