"""
 Write a function to compare 2 numbers.
E.g. compare(2, 3) should return False otherwise should return True.
"""


def compare_numbers(x, y):
    if x > y:
        return f"{x} is more than {y}"
    else:
        return f"{y} is more than {x}"


print(compare_numbers(4, 6))
print(compare_numbers(5, 2))

""" 
Modify the previous function to compare only positive numbers.
In case of negative numbers it will return a print statement like: "Can compare only positive numbers!".
"""


def compare_numbers2(x, y):
    if x < 0 or y < 0:
        return "Can compare only positive numbers!"
    elif x > y:
        return f"{x} is more than {y}"
    elif x < y:
        return f"{y} is more than {x}"


print(compare_numbers2(-4, -66))
print(compare_numbers2(-1, 2))

"""
Write a function to sum 2 numbers.
E.g. add(4, 5) should return 9 as a result.
"""


def sum(x, y):
    return x + y


print(sum(5, 4))

"""
Write a function to subtract 2 numbers.
E.g. sub(4, 2) should return 2 as a result.
"""


def subtract(x, y):
    return x - y


print(subtract(4, 2))
print(subtract(4, 8))

"""
Write a function that returns a type of input.
E.g. give_a_type("test") should return a print statement like: "string".
"""


# 1
def give_a_type(x):
    return type(x)


print(give_a_type(1))
print(give_a_type("1"))
print(give_a_type(False))


# 2
def get_type(x):
    if isinstance(x, str):
        return "string"
    if isinstance(x, int):
        return "integer"
    return "unknown"


print(get_type(5))
print(get_type("5"))

""" Write a function that prints input vertically.
E.g. print_vertical("test me please") should return:
t
e
s
t

m
e

p
l
e
a
s
e
"""

def print_vertical(text):
    for letter in text:
        print(letter)

print(print_vertical("Hello test!"))

"""
 Write a function that concatenates 2 strings.
E.g. concat("abc" , "123") should return a print statement like: "adc123".
"""


def concat(text_1, text_2):
    return text_1 + text_2
print(concat("abc", "123"))
