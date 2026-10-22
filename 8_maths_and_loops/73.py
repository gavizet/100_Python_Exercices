"""
73. Utiliser une boucle pour calculer la moyenne d'une liste de nombres.
my_list = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
"""


def mean_of_num_list(my_list: list) -> int:
    result = 0
    for num in my_list:
        if not isinstance(num, int) and not isinstance(num, float):
            return f"{num} is not a valid int :)"
        result += num
    return result / len(my_list)


my_list = [1, 2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
result = mean_of_num_list(my_list)
print(f"Mean of my_list = {result}")
my_list = [3, 3, 3, 3]
result = mean_of_num_list(my_list)
print(f"Mean of my_list = {result}")
my_list = [3, 3, 3, "test"]
result = mean_of_num_list(my_list)
print(f"Mean of my_list = {result}")
my_list = [3.2, 3.1, 3.1, 3.2]
result = mean_of_num_list(my_list)
print(f"Mean of my_list = {result}")
