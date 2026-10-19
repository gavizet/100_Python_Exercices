# 45. Demander à l'utilisateur un nombre et afficher tous les nombres de 1 à ce nombre, sauf ceux divisibles par 4. 

i = 0
number = 1
result = []
try:
    number = int(input("Give me a positive number: "))
except:
    print("That's not a valid number")
while i <= number:
    if i % 4 == 0:
        i += 1
        continue
    else:
        result.append(i)
        i += 1
print(result)