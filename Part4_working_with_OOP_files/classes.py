class Person:
    name = ""
    dob = ""

    def age(self):
        return "test age 20"

    """def in class called method, it is belongs to this specific class"""
    def get_age(self):
        print(self.age())

person_1 = Person()
person_1.name = "John"
# person_1.dob = "03/28/2002"
# person_1.age = "20 years old"
(person_1.get_age())

print(person_1.name, person_1.age, person_1.dob)