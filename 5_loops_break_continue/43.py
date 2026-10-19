# 43. Utiliser continue pour afficher uniquement les nombres impairs de 1 à 10.

i = 1
result = []
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    result.append(i)
    i += 1
print(result)