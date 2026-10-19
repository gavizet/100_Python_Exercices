# 16. Vérifier si un nombre est divisible à la fois par 2 et par 3, mais pas par 9

def num_div_2and3_not_9(num: int) -> bool:
    if num % 2 == 0 and num % 3 == 0 and not num % 9 == 0:
        return True
    return False

nums = [-12, 0, 10, 12, 18, 25]
# exp [True, False, False, True, False, False]
for number in nums:
    print(f"{number} is div by 2 and 3, but NOT 9: {num_div_2and3_not_9(number)}")