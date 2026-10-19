# 20. Écrire un programme qui vérifie si un nombre est à la fois positif, pair et supérieur à 100

def num_pos_even_higherthan100(num: int) -> bool:
    if num > 0 and num % 2 == 0 and num > 100:
        return True
    return False

nums = [-12, 0, 99, 100, 102, 2000, 2001]
# exp [False, False, False, False, True, True, False]
for number in nums:
    print(f"{number} is pos, even, and higher than 100: {num_pos_even_higherthan100(number)}")