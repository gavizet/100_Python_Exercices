# 17. Demander à l'utilisateur un nom d'utilisateur et un mot de passe, et vérifier si les deux sont corrects

def ask_username_and_pwd(username_input: str, pwd_input: str) -> None:
    username = str(input(username_input))
    if username != "gaetan":
        raise ValueError("Invalid username, expected 'gaetan'")
    password = str(input(pwd_input))
    if password != "test password":
        raise ValueError("Invalid password, expected 'test password'")

ask_username_and_pwd("Type your username (gaetan): ", "Type your password (test password): ")