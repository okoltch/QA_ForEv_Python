# 1) Write a program to print result like(use loop):
# H
# e
# l
# l
# o
#
# P
# y
# t
# h
# o
# n
# !

# # import string
# # s = string.ascii_lowercase
# # a = 1
# # while a <11:
# #     print(f'{a} {s[a - 1]}')
# #     a +=1
#
# for letter in "Hello Python!":
#     print(letter)

#
# Write a program that uses loop and prints numbers from 1 to 100
#    but the program should stop if a number is equal to 45.
# i = 1
# while i <= 100:
#     print(i)
#     if i == 45:
#         break
#     i += 1

# # 4.3 1. Write a program that prints even numbers from 1 to 20.
#
# for x in range(1, 21):
#     if x % 2 == 0:
#         print(x)
#
# # 2.Write a program that prints odd numbers from 1 to 30.
# for x in range(1, 21):
#     if x % 2 != 0:
#         print(x)

# 4.4
#   1) Write a program that prints numbers from 30 to 0 in decreasing order
# i = 1
# for i in reversed(range(1, 31)):
#     print(i)

# #drugoe reshenie
# for i in range(30, -1, -1):
#     print(i)

# 4.4 Write a program that prints first 10 letters from ABC, the results should be like:
# 1 a
# 2 b
# 3 c
# 4 d
# 5 e
# 6 f
# 7 g
# 8 h
# 9 i
# 10 j
# import string
# s = string.ascii_lowercase
# # i = 1
# for i in range(1, 11):
#     print(f'{i} {s[i - 1]}')
    # i += 1

# Other solution
#
# abc = "abcdefghij"
#
# for i in range(1, 11):
#     print(i, abc[i-1])
