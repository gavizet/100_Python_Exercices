# 42. Créer une boucle qui demande un nombre et s'arrête si le nombre est 0.

num = 1
while num != 0:
    num = input("Give me a number. Type 0 to stop. => ")
    try:
        if int(num) == 0:
            break
    except:
        print("Need a valid number")