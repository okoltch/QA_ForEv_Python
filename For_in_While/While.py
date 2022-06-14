x= 0
while x < 10:
    print(x)
    x = x + 2
##############################################################
x = 20
while x > 10:
    print(x)
    x = x - 1
##############################################################
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

    # Note that number 3 is missing in the result
##############################################################
"""На вход в програму подается последлваткльггсть слов, каждое слово на отдельной
 строке. Концом последлвательности явл слово "END" без кавычек. Напишите программу, которая 
 выводит члены данной последоательности 
"""
# string = input()
# while string != "END":
#     print(string)
#     string = input()
#
string = input()
while string != "END" and string != "end":
    print(string)
    string = input()
