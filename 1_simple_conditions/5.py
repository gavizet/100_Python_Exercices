# 5. Vérifier si un nombre est pair ou impair


def odd_or_even(num: int) -> str:
    if num % 2 == 0:
        return "Even"
    return "Odd"


nums = [1, 2, 0, 9, 10]
for num in nums:
    print(f"{num} is : {odd_or_even(num)}")
