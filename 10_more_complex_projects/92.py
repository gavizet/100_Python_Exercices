"""
92. Trouver le plus grand et le plus petit nombre dans une liste.
numbers = [1, 2, 3, 4, 5]
"""
# That's still not complex bruv

numbers = [1, 2, 3, 4, 5, 0, 789, -12]


min = 0
max = 0
for num in numbers:
    if num < 0:
        min = num
    if num > 0:
        max = num
print(f"Max is : {max} - Min is {min}")
