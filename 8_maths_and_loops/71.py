"""
71. Créer une boucle qui affiche tous les nombres premiers entre 1 et 100.
"""


def is_prime_num(number: int) -> bool:
    if number < 2:
        return False
    # Will stop the loop at n-1, so it doesn't try n%n, which would always give 0
    for index in range(2, number):
        if number % index == 0:
            return False
    return True


print("Prime numbers between 1 and 100:")
for num in range(2, 101, 1):
    if is_prime_num(num):
        print(num, end=" ")
print()
