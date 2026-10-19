# 11. Écrire un programme qui vérifie si un nombre est compris entre 10 et 20.

def is_num_between_10_and_20(num: int) -> bool:
    if num >= 10 and num <= 20:
        return True
    return False

nums = [9, 10, 15, 20, 25]
for number in nums:
    print(f"{number} is between 10 and 20 (inclusive): {is_num_between_10_and_20(number)}")