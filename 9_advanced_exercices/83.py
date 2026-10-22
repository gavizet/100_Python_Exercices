"""
83. Créer une boucle qui parcourt une liste de listes et affiche la somme de chaque
sous-liste.
elements = [
    [5, 89, 79, 4, 12],
    [8, 9, 12, 52, 7, 9],
    [71, 4689, 1, 3],
]
"""


def sum_of_list(list_of_lists: list) -> None:
    for one_list in list_of_lists:
        if not isinstance(one_list, list):
            print("Not a list")
        if all(isinstance(n, int) for n in one_list):
            print(f"Sum of {one_list}: {sum(one_list)}")
        else:
            print("Not a valid sublist, should only be made of int")


elements = [
    [5, 89, 79, 4, 12],
    [8, 9, 12, 52, 7, 9],
    [71, 4689, 1, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ["type", "test"],
]
sum_of_list(elements)
