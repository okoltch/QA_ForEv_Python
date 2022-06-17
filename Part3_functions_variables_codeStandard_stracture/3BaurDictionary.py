my_dictionary = {
    "name": "John",
    "last_name": "Doe",
    "DOB": "2022-03-21",
    "Note": "Likes Python!"
}
print(my_dictionary)
my_dictionary["name"] = "Sara"
print(my_dictionary)
print(my_dictionary["last_name"])
###############################
#1 Create new dictionary
dict= {
    "Name": "Vasya",
    "age": 41
}

#2 Add new key  element with type of str and value int
dict.update({"salary": 2000})
print(dict)

#3 Add new element with type of tupple and with list value
dict.update({("adress", "state"): ["123 Bubble st.", "CA"]})
print(dict)

#4 Get element by a key
print(dict["Name"])

#5 Delete element by a key
dict.pop(("adress", "state"))
print(dict)

#6 To get list of dictionary keys

print("dictionary list is: ", dict.keys())