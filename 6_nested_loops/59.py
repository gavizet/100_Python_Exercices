'''
59. Créer une grille de caractères où chaque ligne et colonne est remplie de l'indice correspondant
'''

original_list = [
    ['t', 'h', 'i', 's'],
    ['i', 's'],
    ['a'],
    ['t', 'e', 's', 't'],
    []
]

for x, my_list in enumerate(original_list):
    for y, char in enumerate(my_list):
        original_list[x][y] = y
print(original_list)