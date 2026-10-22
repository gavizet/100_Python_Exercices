"""
74. Écrire une boucle qui vérifie si un nombre est un palindrome numérique.
"""


def is_palindrom_of_num_list(my_num: int) -> bool:
    if not isinstance(my_num, int):
        return f"{my_num} is not a valid int :)"
    my_string = str(my_num)
    return my_string == my_string[::-1]


test1 = 123454321
result = is_palindrom_of_num_list(test1)
print(f"{test1} is a numerical palindrome: {result}")
assert result == True

test2 = 123454320
result = is_palindrom_of_num_list(test2)
print(f"{test2} is a numerical palindrome: {result}")
assert result == False

test3 = 0
result = is_palindrom_of_num_list(test3)
print(f"{test3} is a numerical palindrome: {result}")
# assert result == False
