'''
55. Créer une boucle qui parcourt deux listes de mêmes longueurs simultanément et 
affiche leurs éléments côte à côte. 
list_0 = [5, 89, 79, 4, False] 
list_1 = [8, 9, 12, 'azed', 7.7]
'''

list_0 = [5, 89, 79, 4, False] 
list_1 = [8, 9, 12, 'azed', 7.7]

if len(list_0) == len(list_1):
    for i in range(len(list_0)):
        print(list_0[i], list_1[i])
else:
    print("Need lists of same length")