''' 40. Écrire un programme qui demande à l'utilisateur de saisir des nombres positifs et de les ajouter à une liste. Le programme doit continuer à demander des nombres tant que la longueur de la liste ne dépasse pas 5.
'''

i = 0
result = []
number = 0
while i < 5:
    try:
        number = int(input("Give me a positive number:"))
    except:
        print("I need a positive number: ")
    if number > 0:
        result.append(number)
        i += 1
print(result)