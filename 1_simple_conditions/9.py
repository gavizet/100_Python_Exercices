# 9. Créer un programme qui vérifie si une lettre est une voyelle ou une consonne.

def is_vowel(letter) -> bool:
    vowels = "aeiouAEIOU"
    if not isinstance(letter, str):
        return False
    if letter in vowels:
        return True
    return False

letters = ['a', 'y', 'e', 'h', 9]
for lett in letters:
    print(f"{lett} is a vowel: {is_vowel(lett)}")