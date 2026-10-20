'''
62. Utiliser une boucle pour vérifier si une liste est triée ou non. 
my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
'''

def list_is_sorted(my_list: list) -> bool:
    biggest = None
    for elem in my_list:
        if biggest is None:
            biggest = elem
        if biggest > elem:
            return False
    return True

my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"{my_list} is sorted: {list_is_sorted(my_list)}")
print(f"{my_list2} is sorted: {list_is_sorted(my_list2)}")