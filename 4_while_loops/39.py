# 39. Afficher les nombres pairs de 2 à 200 s'ils sont divisibles par 3 avec une boucle while. 

i = 2
result = []
while i <= 200:
    if i % 2 == 0 and i % 3 == 0:
        result.append(i)
    i += 1
print(result)