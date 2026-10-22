"""
77. Créer une boucle qui génère et affiche les carrés des nombres de 1 à 20.
"""


def square(num: int) -> int:
    if isinstance(num, int):
        return num * num
    return None


def list_squares_list(highest_num: int):
    for num in range(highest_num + 1):
        print(f"{num}^2 = {square(num)}")


# TEST 1
test1 = 20
result = list_squares_list(test1)
