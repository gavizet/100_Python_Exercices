# 2. Vérifier si un nombre donné est positif, négatif ou nul.

def num_pos_neg_zero(num):
    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative"
    return "Positive"

nums = [8, -8, 0, 12345678, -12345678]
for num in nums:
    print(f"{num} is {num_pos_neg_zero(num)}")