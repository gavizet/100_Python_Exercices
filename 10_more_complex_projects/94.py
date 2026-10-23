"""
94. Calculer la somme des diviseurs d’un nombre donné.
"""


def sum_of_dividors(num: int) -> int:
    """Gets the sums of dividors for a given number

    Args:
        num (int): The number we want to find the dividors from

    Returns:
        divisors (int): the sum of the dividors
    Raises:
        TypeError: if the given number is not valid, aka not an int or float
    """
    if num < 0 or not isinstance(num, int):
        return "Invalid input - expected a positive integer"
    divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisors += i
    return divisors


all_tests = [-5, 0, 1, 3, 5, 10, 21, 24, 97, 240]
for test in all_tests:
    print(f"Sum of dividors of {test}: {sum_of_dividors(test)}")
