file = open("text.txt", "r")
"""To read the whole file"""
# print(file.read())


"""To read file by rows"""
# print(file.readline())
# print(file.readline())

"""To red file by symbols"""
# print(file.read(4))


for line in file:
    print(line)


"""You always have to close file. """
file.close()