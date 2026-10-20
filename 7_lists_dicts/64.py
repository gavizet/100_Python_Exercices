'''
64. Créer un programme qui enlève tous les éléments d'une liste qui sont inférieurs à 10. 
my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
'''

def pop_list_elem(my_list: list) -> list:
    return [elem for elem in my_list if elem >= 10]

my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
print(my_list)
filtered_list = pop_list_elem(my_list)
print(filtered_list)