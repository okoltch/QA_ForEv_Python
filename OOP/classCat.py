class  Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print(f"Cat {self.name} is being initialized and says Meow!")

    def say_meow(self):
        print(f" {self.name} says Meow!")

    def print_name(self):
        print("This is ", self.name)

    def print_age(self):
        print(f"{self.name} is {self.age} years old")

    def print_weight(self):
        print(f"{self.name}'s weight is {self.weight} ")

    def print_all_characteristics(self):
        print(f"This is {self.name}. He is {self.age} years old, and his weight is {self.weight} pounds.")

    def eat(self, food):
        print(f"{self.name} ate {food}")

    def eat_a_lot(self, food="food"):
        self.weight += 0.25
        print(f"{self.name} ate a lot of {food}, and gained quoter pound.")

black_cat = Cat("Tom", 2, 8.5)

black_cat.print_name()
black_cat.print_age()
black_cat.print_weight()
black_cat.print_all_characteristics()
black_cat.eat("fish")
black_cat.eat_a_lot("chicken")
black_cat.print_weight()


gray_cat = Cat("Lucky", 3, 14)
print(gray_cat)
gray_cat.print_all_characteristics()



