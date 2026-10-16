# 4. Écrire un programme qui vérifie si une chaîne de caractères est vide ou nondef is_an_adult(age):

def is_string_empty(my_str: str) -> str:
    if my_str == "":
        return "Empty string"
    return "Non empty string"

strings = ["test", "", "coucou", 9]
for one_string in strings:
    print(f"String is : {is_string_empty(one_string)}")