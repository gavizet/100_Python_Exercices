# 15. Écrire un programme qui vérifie si une chaîne de caractères contient la lettre 'a'.

def string_contains_a(string: str) -> bool:
    if 'a' in string:
        return True
    return False

test_strings = ['', "test", "hablo espanol", "hello"]
# expected: [False, False, True, False]
for my_string in test_strings:
    print(f"'{my_string}' contains 'a': {string_contains_a(my_string)}")