"""7.1 Create a program/function that gets a parameter as a text,
    creates file "text.txt" and inserts the text into the file.
    As the result of the program/function, we have to get our file "text.txt"
    with the content from the parameter."""
#1 My solution
def create_file(x):
    with open("text.txt", "w") as file:
         file.write(x)

print(create_file("hello"))


# 2 Teacher solution
def create_a_file_with_text(text: str) -> None:
    with open("text.txt", 'w') as file:
        file.write(text)




