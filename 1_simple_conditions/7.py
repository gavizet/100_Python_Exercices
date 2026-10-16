# 7. Vérifier si un nombre est divisible par 3 ou par 5.

numbers = [10, 15, 21, 22, 0]
for num in numbers:
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} divisible by 3 AND 5")
    elif num % 3 == 0 and not num % 5 == 0:
        print(f"{num} divisible by 3 but NOT 5")
    elif not num % 3 == 0 and num % 5 == 0:
        print(f"{num} divisible by 5 but NOT 3")
    else:
        print(f"{num} NOT divisible by 5 OR 3")