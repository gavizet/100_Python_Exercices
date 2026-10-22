"""
81. Créer un programme qui vérifie si deux chaînes sont des anagrammes.
"""


def is_anagram(str1: str, str2: str) -> bool:
    return sorted(str2.lower()) == sorted(str1.lower())


# TEST 1
str1 = "Iam Lord Voldemort"
str2 = "Tom Marvolo Riddle"
print(is_anagram(str1, str2))
# TEST 2
str3 = "test"
str4 = "tset"
print(is_anagram(str3, str4))
# TEST 3
str5 = "fail test"
str6 = "failed test"
print(is_anagram(str5, str6))
