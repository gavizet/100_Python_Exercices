'''
68. Utiliser une boucle pour trouver l'élément le plus grand dans une liste. 
my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
'''

my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
curr_max = 0
for elem in my_list:
    if elem > curr_max:
        curr_max = elem
print(f"Biggest element in {my_list} is {curr_max}")