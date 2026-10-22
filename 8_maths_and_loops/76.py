"""
76. Utiliser une boucle pour vérifier si un nombre est parfait.
"""


def get_all_dividors(num: int) -> list:
    dividors_list = []
    for i in range(1, num):
        if num % i == 0:
            dividors_list.append(i)
    return dividors_list


def is_perfect_number(num: int) -> bool:
    if not isinstance(num, int) or num <= 0:
        return "Not a valid number, need to be an int > 0"
    dividors = get_all_dividors(num)
    return num == sum(dividors)


# TEST 1
test1 = 6
result = is_perfect_number(test1)
print(f"{test1} is a perfect number: {result}")
assert result == True
# TEST 2
test2 = 28
result = is_perfect_number(test2)
print(f"{test2} is a perfect number: {result}")
assert result == True
# TEST 3
test3 = 0
result = is_perfect_number(test3)
print(f"{test3} is a perfect number: {result}")
assert result == "Not a valid number, need to be an int > 0"
# TEST 4
test4 = 35
result = is_perfect_number(test4)
print(f"{test4} is a perfect number: {result}")
assert result == False
