# 38. Demander un nombre à l'utilisateur et calculer sa factorielle avec une boucle while.

def get_factorial(num) -> int:
    if num <= 0:
        raise ValueError("A factorial can only be positive.")
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 1
    return factorial


numbers_list = [1, 2, 3, 4, 5]
for number in numbers_list:
    print(f"Factorial of {number} is: {get_factorial(number)}")