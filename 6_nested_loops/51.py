# 51. Écrire un programme qui affiche la table de multiplication de 1 à 10 avec des boucles imbriquées. 

for multiplicand in range(1, 11):
    for multiplier in range(1, 11):
        print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")