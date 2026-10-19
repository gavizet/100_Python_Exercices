# 41. Utiliser une boucle pour afficher les nombres de 1 à 20, mais arrêter dès que vous atteignez 10.

i = 1
while i <= 20:
    if i >= 10:
        break
    print(i)
    i += 1