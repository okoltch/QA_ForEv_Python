#protected, public, private

class Person:
    def __init__(self, name, dob, height, gender):
        self._name = name
        self.__dob = dob
        self.height = height
        self.gender = gender

    def get_name(self):
        return self._name

    def get_dob(self):
        return self.__dob

    def set_dob(self, new_dob):
        self.__dob = new_dob

person_one = Person("John", "May 1, 2000", 6, "M")

print(person_one.get_name())

"""You can change information of already existed person """
person_one._name = "Jane"

"""But dob can not be changed, so we need to restrict access by putting 
.__dob into class construction 
self._    -protected- will be available inside child classes of parent
self.__   -private-  will be available only in a certain class
self.     -public
"""

print(person_one._name)

print(person_one.get_dob())


person_one.set_dob("May 11, 2000")

print(person_one.get_dob())
