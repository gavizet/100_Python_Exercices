'''
52. Créer un programme qui affiche un rectangle de caractères "X" de taille donnée par 
l'utilisateur.
'''

try:
    size = int(input("Give me a size (int and positive) and I will print a rectangle: "))
    if size <= 0:
        raise ValueError("Need a positive number")
    row = size * "X"
    for i in range(0, size):
        print(row)
except:
    print("That's not a number")