'''
54. Afficher tous les éléments d'une liste de listes avec des boucles imbriquées. 
elements = [ 
    [5, 89, 79, 4, False], 
    [8, 9, 12, 'azed', 7.7, 9], 
    [7.12, "aba", 4689, True, 3], 
] 
'''

elements = [ 
    [5, 89, 79, 4, False], 
    [8, 9, 12, 'azed', 7.7, 9], 
    [7.12, "aba", 4689, True, 3], 
]

for list in elements:
    for var in list:
        print(var)