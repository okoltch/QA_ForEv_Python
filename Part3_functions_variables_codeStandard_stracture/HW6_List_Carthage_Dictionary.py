"""
 Write a program/function that prints list entities one by one. As an input use a list.
e.g. print_entities(["a", "b", "c"]) should return:
"a"
"b"
"c"
"""


# 1
def print_entities(myList):
    for i in myList:
        print(i)


print(print_entities("abc"))

# 2
list2 = ["a", "b", "c"]
for i in list2:
    print(i)

"""
 Write a program/function that converts strings into tuples.
e.g. convert("abide") should return tuple like:
("a", "b", "i", "d", "e") 
"""

# 1
text = "abide"
listText = list(text)
tuptext = tuple(text)

print(text)
print(listText)
print(tuptext)


# 2
def convert_string_to_tuple(text):
    new_list = []
    for item in text:
        new_list.append(item)
    return tuple(new_list)


print(convert_string_to_tuple("abide"))

"""
Write a program/function that removes duplicates and returns only unique values as a list.
e.g. remove_dups("abcdadab") should return ["a", "d", "c", "b"]. Note, order of elements in the list is not important!
"""

# 1
remove_dups = "abcdadab"
res = [i for n, i in enumerate(remove_dups) if i not in remove_dups[:n]]
print(res)


# 2
def remove_dups(text):
    return list(set(text))


print(remove_dups("abcdadab"))

"""
 Write a program/function that collects certain data as parameters and returns a dictionary object.
e.g. client("John", "Doe", "01/23/1934", "Male", "San Antonio", "TX", "78261") should return a dictionary object like:
{
	"Name": "John",
	"Lastname": "Doe",
	"DOB": "01/23/1934",
	"Sex": "Male",
	"City": "San Antonio",
	"State": "TX",
	"ZipCode": "78261"
}
"""

dictionary = {
    "Name": "John",
    "Lastname": "Doe",
    "DOB": "01/23/1934",
    "Sex": "Male",
    "City": "San Antonio",
    "State": "TX",
    "ZipCode": 78261
}
print(dictionary)
print(dictionary["Name"])

name = dictionary.get("Name")
lastName = dictionary.get("Lastname")
clientName = name + " " + lastName
print(clientName)