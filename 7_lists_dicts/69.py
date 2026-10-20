'''
69. Créer une boucle qui copie tous les éléments d'une liste dans une autre liste. 
first_list = [8, 9, 'mrt', 97, True, 1.2, 4, 2, 9, 12, 4, 32, 13, 8, 78] 
'''

first_list = [8, 9, 'mrt', 97, True, 1.2, 4, 2, 9, 12, 4, 32, 13, 8, 78] 
second_list = []
for elem in first_list:
    second_list.append(elem)
print(second_list)