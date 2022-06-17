class Alive:
    def __init__(self, eat, breath, reproduce):
        self.eat = eat
        self.breath = breath
        self.reproduce = reproduce


class Mamal(Alive):
    def __init__(self):
        super().__init__("milk", "lungs", "birth")

class Predator(Mamal):
    def __init__(self, eat):
        super().__init__()
        self.eat = eat
        self.feature = "claws"

class Herbivore(Mamal):
    def __init__(self):
        super().__init__()
        self.eat = "grass"
        self.feature = "horns and hooves"
    def print_herbivore(self):
        print(f"This is Herbivore. He likes {self.eat}, and he has {self.feature}")


class Bird(Alive):
    def __init__(self):
        super().__init__("insects", "lungs", "eggs")


class Fish(Alive):
    def __init__(self):
        super().__init__("seaweed", "gills", "caviar")


bobCat = Predator("meat")

print(bobCat.feature)
print(bobCat.eat)

panda =Herbivore()
panda.print_herbivore()

guffi = Fish()
print(guffi.reproduce)
print(guffi.eat)

chizhic = Bird()
print(chizhic.breath)
print(chizhic.eat)
