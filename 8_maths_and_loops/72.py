"""
72. Écrire une boucle qui calcule le produit de tous les éléments d'une liste.
my_list = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
"""


def product_num_list(my_list: list) -> int:
    result = 1
    for num in my_list:
        if not isinstance(num, int):
            return f"{num} is not a valid int :)"
        result *= num
    return result


my_list = [21, 23, 25, 27, 29, 31, 33, 35]
result = product_num_list(my_list)
print(result)
assert result == 338526428625
my_list = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
result = product_num_list(my_list)
print(result)
assert result == 443286190953399543750
