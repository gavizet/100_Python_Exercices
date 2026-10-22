"""
88. Utiliser des boucles pour créer une liste de toutes les paires possibles d'une liste donnée.
my_list = [5, 89, 79, 4, 12]
"""


# Method 1, nested loops
def get_all_possible_pairs(my_list: list) -> list:
    all_pairs = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            all_pairs.append((my_list[i], my_list[j]))
    return all_pairs


# Method 2, list comprehension
def get_all_possible_pairs_2ndway(my_list: list) -> list:
    return [
        (my_list[i], my_list[j])
        for i in range(len(my_list))
        for j in range(i + 1, len(my_list))
    ]


my_list = [5, 89, 79, 4, 12]
result = get_all_possible_pairs(my_list)
print(f"With nested loops:\n{result}")
result = get_all_possible_pairs_2ndway(my_list)
print(f"With list comprehension:\n{result}")
