'''
67. Écrire une boucle qui fusionne deux listes en une seule. 
elements = [8, 9, 'mrt', 97, True, 1.2] 
my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78] 
'''

elements = [8, 9, 'mrt', 97, True, 1.2] 
my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78]

for elem in my_list:
    elements.append(elem)
print(elements)