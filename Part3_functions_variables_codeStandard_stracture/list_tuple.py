my_list = ["banana", "apple", "grapes", "peach"]
my_tuple = (1, "f", 4.6, False)
my_tuple2 = ("Book", "Author", "date", "publisher")
my_shop = ["apple", 5, "$", False, "discount"]

print(my_list)

my_list.append("bluberry")
print(my_list)
my_list.append(4)
print(my_list)
my_list.pop()
print(my_list)
my_list.append("lkds")
print(my_list)
my_list.pop(5)
print(my_list)
my_list.pop(0)
print(my_list)

my_list.insert(0, "banana")
print(my_list)

my_list.append([2, 3, 54])
print(my_list)

my_list.insert(1, [1, "apple", 3, 4])
print(my_list)

my_list.insert(-1, ("one", "two",))
print(my_list)

print(my_list[1])


"""To check for duplicates"""
my_list2 = [1, 2, 3, 3, 2, 1 ,3, 5, 4]
print(set(my_list2))
print(len(my_list2))

print((len(my_list2)) == len(set(my_list2)))
