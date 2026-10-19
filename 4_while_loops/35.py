# 35. Utiliser while pour afficher les multiples de 5 entre 1 et 50

multiples_of_5 = []
i = 0
while i <= 50:
    if i % 5 == 0:
        multiples_of_5.append(i)
    i += 5
print(f"Multiples of 5 between 1 and 50: {multiples_of_5}")