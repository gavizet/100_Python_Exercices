# 47. Utiliser break pour quitter une boucle infinie après 5 itérations.

i = 0
while True:
    if i == 5:
        break
    i += 1
    print(f"Iterations: {i}")