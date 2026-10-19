# 34. Créer une boucle infinie qui demande un mot de passe jusqu'à ce qu'il soit correct.

password = ""
correct_password = "gaetan"

while correct_password:
    try:
        password = str(input("I will keep looping until you guess the password: "))
    except:
        break
    if password == correct_password:
        print("YOU GOT IT!")
        break