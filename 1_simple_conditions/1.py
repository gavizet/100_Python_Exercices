#1. Écrire un programme qui vérifie si un nombre donné est supérieur à 10.
def num_higher_than_10(num):
    if num > 10:
        return True
    return False

nums = [8, 9, 10, 11, 12]
for num in nums:
    print(f"Is {num} > 10 ? {num_higher_than_10(num)}")
