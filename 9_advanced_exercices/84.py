"""
84. Utiliser une boucle pour trier une liste de tuples en fonction de la deuxième valeur.
elements = [
    (71, 4689, 1, 3),
    (5, 89, 79, 4, 12),
    (8, 9, 12, 52, 7, 9),
    (9, 1, 567, 10, 11)
]
"""
# Doc: https://www.w3schools.com/python/ref_list_sort.asp
# For how to sort list with a key function


def sort_by_2nd_value(e):
    return e[1]


def sum_of_list(list_of_tuples: list) -> list:
    for my_tuple in list_of_tuples:
        if not isinstance(my_tuple, tuple):
            print(my_tuple)
            return "Not a tuple"
        if len(my_tuple) < 2:
            return "Need 2 elems min per tuple to filter"
        if not isinstance(my_tuple[1], int):
            return "Not a valid tuple, should only be made of int"
    list_of_tuples.sort(key=sort_by_2nd_value)
    return list_of_tuples


elements = [
    [
        (71, 4689, 1, 3),
        (5, 89, 79, 4, 12),
        (8, 9, 12, 52, 7, 9),
        (9, 1, 567, 10, 11),
    ],
    [
        (71, 4689, 1, 3),
        (5, 89, 79, 4, 12),
        (8, 9, 12, 52, 7, 9),
        (9, 1, 567, 10, 11),
        ("little", "test"),
    ],
    [
        (71, 4689, 1, 3),
        (5, 89, 79, 4, 12),
        (8, 9, 12, 52, 7, 9),
        (9, 1, 567, 10, 11),
        (1),
    ],
]
for elem in elements:
    print(sum_of_list(elem))
