# 8. Demander à l'utilisateur un mot de passe et vérifier s'il correspond à "admin".

password = input("Type your password - hint, it's 'admin':")
if password == "admin":
    print("Excellent reading skills")
else:
    print("You are a dimwit")