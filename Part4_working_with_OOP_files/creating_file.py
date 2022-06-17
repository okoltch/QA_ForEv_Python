# file = open("text_1.txt", "w")
#
# file.write("my super text!")
#
# file.close()


""" With this method we don't need to close the file"""
with open("text_2.txt", "x") as file:
    file.write("Some dummy text")



