'''
58. Créer une boucle imbriquée pour générer les coordonnées (x, y) d'un quadrillage de 0 à 4.
'''

def print_coords(x_coords: int, y_coords: int) -> None:
    for i in range(x_coords, -1, -1):
        for j in range(y_coords+1):
            print(f"{(i, j)}", end="")
        print()

print_coords(4, 4)