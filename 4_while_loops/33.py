# 33. Demander à l'utilisateur un nombre et continuer à demander tant que ce nombre est négatif

num = 0
while quit:
    try:
        num = int(input("Give me a negative number. If you want to leave, give me anything else: "))
    except:
        break
    if num >= 0:
        break