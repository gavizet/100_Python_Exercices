'''
46. Créer une boucle qui affiche les éléments d'une liste mais s'arrête dès qu'elle 
rencontre un élément spécifique. 
elements = ['apple', 'banana', 'cherry', 'orange', 'grape'] 
stop_element = 'cherry' 
'''

elements = ['apple', 'banana', 'cherry', 'orange', 'grape'] 
stop_element = 'cherry' 
for elem in elements:
    print(f"Current Element: {elem}")
    if elem == stop_element:
        print("Stopping")
        break