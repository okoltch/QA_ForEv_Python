def inc_function(x):
    """Increase X by 1"""

    x = x + 1
    print(x)

inc_function(3)

def sum_function(x, y):
    print(x + y)

sum_function(-5, 6)


"""My program"""

def my_function2(x, y):
    z = (x + y) / 2
    text = f"Result of calculation: {z}"
    print(text)

a1 = 14
b1 = 23
my_function2(a1, b1)

a2 = 45
b2 = 56
my_function2(a2, b2)

a3 = -56
b3 = 7
my_function2(a3, b3)

"""My program 2"""
def sum_function2(x, y):
    result = x + y
    return result

a1 = 14
b1 = 23
res = sum_function2(a1, b1)
print(f"result: {res}")

a2 = 45
b2 = 56
res = sum_function2(a2, b2)
print(f"result: {res}")

a3 = -56
b3 = 7
res = sum_function2(a3, b3)
print(f"result: {res}")

"""My program 3"""
def compare_function(x, y):
    if x > y:
        return True
    else:
        return False

print(compare_function(3, 4))



"""My program 4"""
x = 45
def dummy_function():

    x = 12
    x += 1
    return x

dummy_function()
print(x + dummy_function())

"""My program 5"""
x = 45
def dummy_function():
    global x
    x = 12
    x += 1
    return x

dummy_function()
print(x + dummy_function())

"""My program 6"""
x = 45
def dummy_function():
    global x
    y = x
    y += 1
    return y

dummy_function()
print(x + dummy_function())
