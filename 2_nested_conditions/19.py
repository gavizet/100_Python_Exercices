# 19. Créer un programme qui vérifie si une chaîne de caractères est un palindrome.

def is_string_a_palindrome(my_string: str) -> bool:
    if my_string == my_string[::-1]:
        return True
    return False

test_strings = ["kayak", "abcdedcba", "this is a test", "nein nein nein"]
for test_string in test_strings:
    print(f"{test_string} is a palindrome: {is_string_a_palindrome(test_string)}")