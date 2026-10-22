"""
82. Écrire une boucle qui parcourt un texte et compte le nombre de mots.
"""


# I assume words are only made of alphanumeric characters
def count_words(string: str) -> int:
    words_num = 0
    check_next = 1
    for char in string:
        # If current char is not alphanumeric, put check_next at 1
        if not char.isalnum():
            check_next = 1
        # On next loop, if char IS alnum, if check_next == 1, it means the previous char was NOT alnum, so this is a new word. Increment words_num by 1, and reset our check_next
        elif char.isalnum() and check_next == 1:
            words_num += 1
            check_next = 0
    return words_num


all_tests = ["     ", "", "test", "t e s t", " t,e;s|t ?", "this is a simple test"]
for test in all_tests:
    result = count_words(test)
    print(f"{test} contains {result} words")

test = "t e s t"
result = count_words(test)
print(f"{test} contains {result} words")
