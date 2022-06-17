"""
8.1 Use an object from the real world to create a class in Python
"""

class Food:
    def __init__(self, name):
        self.name = name
        self.cook_time = 0
        self.type = ""

    def when_to_cook(self):
        pass

class Cake(Food):
    def __init__(self, name):
        super(Cake,self).__init__(name)
        self.cook_time = 60
        self.type = "sweet"

    def when_to_cook(self):
        print("for tea")

class Steak(Food):
    def __init__(self, name):
        super(Steak, self).__init__(name)
        self.cook_time = 25
        self.type = "meat"

    def when_to_cook(self):
        print("dinner")

class Eggs(Food):
    def __init__(self, name):
        super(Eggs, self).__init__(name)
        self.cook_time = 5
        self.type = "protein"

    def when_to_cook(self):
        print("morning")

cake = Cake("Napoleon")
print(cake.name)
print(cake.type)
print(cake.cook_time)
cake.when_to_cook()

steak = Steak("Rib Eye")
print(steak.name)
print(steak.type)
print(steak.cook_time)
steak.when_to_cook()

eggs = Eggs("Scrumbled")
print(eggs.name)
print(eggs.type)
print(eggs.cook_time)
eggs.when_to_cook()