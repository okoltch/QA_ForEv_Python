class Table():
    def __init__(self, color, shape):              #эта конструкция создаст наш класс
        self.color = color
        self.shape = shape

    my_property = "test property"

    def get_my_property(self):
        print(self.my_property)

my_table = Table("red", "circle")

print(my_table.color)
print(my_table.shape)
print(my_table.my_property)