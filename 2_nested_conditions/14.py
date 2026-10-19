# 14. Vérifier si un nombre est positif et multiple de 5. 

def is_num_pos_and_multiple_of_5(num: int) -> bool:
    if num >= 0 and num % 5 == 0:
        return True
    return False

nums = [-12, 0, 10, 12, 18, 25]
# exp [False, True, True, False, False, True]
for number in nums:
    print(f"{number} is positive and divisible by 5 {is_num_pos_and_multiple_of_5(number)}")