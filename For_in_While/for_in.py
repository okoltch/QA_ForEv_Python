# for i in range(3):
#     if i <= 1:
#         print("Hi!")
#     else:
#         print("Good morning!")
#
#
# m = 2
# n = 4
# for i in range(m, n+1):
#     i =int(input())
#     if i > 5:
#         print(i)
#     print("Element ", i)
#
# print("m", m)



# s = "Hello!"
# for i in range(10):
#     print(i, s)


# s = "Hello!"
# for i in range(1, 11):
#     print(i, s)

#
# s = "Hello!"
# for i in range(10):
#     print(i + 1, s)



n = 6
for i in range(n):
    print("*" * (n - i))


"""
m:starting number of items
p: increasement of item in 50%
n: number of days to multiply
Write a program that will show how items grow.
Programm have to show incresement per each da, starting from 1
and finishing witn n day

"""
m = 10
p = 50
n = 6

#
# for i in range(n):
#     print(f'{i + 1} {m}')
#     m+= m * (p / 100)

for i in range(n):
    m = m + m * (p / 100)
    print(f'On the {i} day we have {m} organisms')


""" 
Two numbers are given m and n. Write a program to write all numbers from m to n including 
in ascending order, if m < n, or in descending if m > n"""

# m = 11
# n = 8
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, - 1):
#         print(i)


"""
Two numbers are given, m and n (m > n). Write a programm, that will return all odd numbers
from m to n including in descending order
"""
m = 9
n = 1

for i in range(m, n - 1, - 1):
    if i % 2 != 0:
        print(i)

