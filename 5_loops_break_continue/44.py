# 44. Écrire une boucle qui affiche les nombres de 1 à 20, mais saute les multiples de 3.

i = 1
result = []
while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    result.append(i)
    i += 1
print(result)