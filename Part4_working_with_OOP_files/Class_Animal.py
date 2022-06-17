class Animal:
    def __init__(self, name):
        self.name = name
        self.weight = 0

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)                 #Super methor calls parent
        self.weight = 10

    def speak(self):
        print("woof")

class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)
        self.weight = 4

    def speak(self):
        print("meow")


class Bird(Animal):
    def __init__(self, name):
        super(Bird, self).__init__(name)
        self.weight = 0.5

    def speak(self):
        print("tweet")

class Fish(Animal):
    def __init__(self, name):
        super(Fish, self).__init__(name)
        self.weight = 0.2

animal = Animal("animal")
animal.speak()
print(animal.weight)



dog = Dog("barsik")
print(dog.name)
dog.speak()
print(dog.weight)

cat = Cat("pepsi")
print(cat.name)
cat.speak()
print(cat.weight)

bird = Bird("tweeter")
print(bird.name)
bird.speak()
print(bird.weight)

fish = Fish("karp")
print(fish.name)
fish.speak()
print(fish.weight)

