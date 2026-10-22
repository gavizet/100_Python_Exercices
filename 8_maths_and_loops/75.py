"""
75. Créer une boucle qui calcule les 10 premiers termes de la suite de Fibonacci.
"""
# Nice, I've only done this exercice 25 times!
# Actually struggled a bit, I am braindead


def fibonacci(num: int) -> int:
    f0, f1 = 0, 1
    for i in range(num):
        # print(f"f0: {f0}", end=", ")
        # print(f"f1: {f1}", end=", ")
        f0, f1 = f1, f0 + f1
        # print(f"f0: {f0}", end="\n")
    return f0


# TEST 1
num = 6
result = fibonacci(num)
print(f"Fibonacci of {num} = {result}")
assert result == 8
# TEST 2
num = 10
result = fibonacci(num)
print(f"Fibonacci of {num} = {result}")
assert result == 55
# TEST 3
num = 100
result = fibonacci(num)
print(f"Fibonacci of {num} = {result}")
assert result == 354224848179261915075
