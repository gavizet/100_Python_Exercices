"""
80. Utiliser une boucle pour déterminer si deux listes sont identiques.
my_list_0 = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
my_list_1 = [1, 2, 3, 5, 7, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 9, 11, 13, 15]
"""


# I am assuming we want to know if lists have all the same values, otherwise exercice makes no sense.
def are_lists_identical(list1: list, list2: list) -> bool:
    for i, elem in enumerate(list1):
        if elem not in list2:
            return False
    return True


my_list_0 = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
my_list_1 = [1, 2, 3, 5, 7, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 9, 11, 13, 15]

print(are_lists_identical(my_list_0, my_list_1))
