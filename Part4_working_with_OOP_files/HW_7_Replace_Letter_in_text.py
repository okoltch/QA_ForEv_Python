"""7.2 Create a program/function that gets 2 parameters,
    first parameter a file name,
    second parameter character (letter, number)
    and replaces all characters in the file to 0 which equals the second parameter.
    E.g. we have a file "my_text.txt" with the text "Hello Python! Lesson 7",
    we pass the second parameter as "e" to the program/function, and as the result
    text in the file will be "H0llo Python! L0sson7"
"""

def replace_to_zero(file_name: str, letter:str) ->None:
    with open(file_name, "w") as file:
        file.write(letter)

    transformed = letter.replace("o", "0")

    with open(file_name, "w") as file:
        file.write(transformed)

print(replace_to_zero("my_text.txt", "Hello Python"))