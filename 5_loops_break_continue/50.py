'''
50. Afficher les éléments d’une liste, arrêter la boucle si un même élément apparaît une deuxième fois. 
elements = ['apple', 'banana', 'cherry', 'orange', 'grape', 'apple', 'banana', 'cherry', 'orange', 'grape'] 
'''

elements = ['apple', 'banana', 'cherry', 'orange', 'grape', 'apple', 'banana', 'cherry', 'orange', 'grape'] 
my_list = []
for elem in elements:
    if elem in my_list:
        break
    print(f"Current element: {elem}")
    my_list.append(elem)
print(f"Full list: {my_list}")