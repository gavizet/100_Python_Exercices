'''
60. Afficher les éléments en diagonale d'une matrice carrée. 
'''

matrix = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
]

for x in range(len(matrix)):
    for y in range(len(matrix)):
        if x == y:
            print(matrix[x][y])

# OR

print([matrix[x][x] for x in range(len(matrix))])