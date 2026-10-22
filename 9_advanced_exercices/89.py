"""
89. Créer une boucle qui recherche tous les indices d'une valeur spécifique dans une liste.
my_list = [5, 89, 12, 5, 89, 79, 4, 12, 5, 12, 5, 89, 79, 4, 12, 5, 89, 79, 4, 12]
n = 12
"""


def get_indexes_of_n(lst: list, n: int) -> list:
    indexes = []
    for index, num in enumerate(lst):
        if num == n:
            indexes.append(index)
    return indexes


my_list = [5, 89, 12, 5, 89, 79, 4, 12, 5, 12, 5, 89, 79, 4, 12, 5, 89, 79, 4, 12]
n = 12
result = get_indexes_of_n(my_list, n)
print(result)
assert result == [2, 7, 9, 14, 19]
result = get_indexes_of_n([0, 1, 2, 3, 3, 3], 3)
print(result)
assert result == [3, 4, 5]
result = get_indexes_of_n([], 3)
print(result)
assert result == []
