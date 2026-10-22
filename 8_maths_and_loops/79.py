"""
79. Créer une boucle qui calcule la somme des chiffres d'un nombre donné.
"""


def sum_of_digits(num: int) -> int:
    my_sum = 0
    for i in range(num + 1):
        my_sum += i
    return my_sum


# TEST 1
test1 = 0
result = sum_of_digits(test1)
print(f"Sum of all digits of {test1} = {result}")
assert result == 0
# TEST 2
test2 = 5
result = sum_of_digits(test2)
print(f"Sum of all digits of {test2} = {result}")
assert result == 15
# TEST 3
test3 = 10
result = sum_of_digits(test3)
print(f"Sum of all digits of {test3} = {result}")
assert result == 55
test4 = 20
result = sum_of_digits(test4)
print(f"Sum of all digits of {test4} = {result}")
assert result == 210
