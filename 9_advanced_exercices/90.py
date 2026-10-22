"""
90. Écrire une boucle qui divise une liste en plusieurs sous-listes de taille égale.
my_list = [5, 89, 12, 592, 9, 79, 4, 812, 15, 142, 1, 76, 5, 89, 79, 4, 12, 598, 8, 79, 4, 128, 21]
"""


def greatest_common_divisor(num: int) -> int:
    for i in range(num - 1, 1, -1):
        if num % i == 0:
            return i
    return 0


def split_list_into_equal_sublists(lst: list) -> list:
    lst_len = len(lst)
    final_lists = []
    gcdivisor = greatest_common_divisor(lst_len)
    if gcdivisor == 0:
        print(
            "Cannot divide into equal sized sublists, no greater common divisor higher than 1"
        )
        return lst
    sub_lists_len = lst_len // gcdivisor
    print(
        f"List of len: {lst_len} can be divided into {gcdivisor} lists of size {sub_lists_len}"
    )
    for i in range(0, lst_len - sub_lists_len + 1, sub_lists_len):
        final_lists.append(lst[i : i + sub_lists_len])
    return final_lists


my_list = [
    5,
    89,
    12,
    592,
    9,
    79,
    4,
    812,
    15,
    142,
    1,
    76,
    5,
    89,
    79,
    4,
    12,
    598,
    8,
    79,
    4,
    128,
    21,
]
result = split_list_into_equal_sublists(my_list)
assert result == my_list
print(result)
my_list = [
    5,
    89,
    12,
    592,
    9,
    79,
    4,
    812,
    15,
    142,
    1,
    76,
    5,
    89,
    79,
    4,
    12,
    598,
    8,
    79,
    4,
]
result = split_list_into_equal_sublists(my_list)
print(result)
assert result == [
    [5, 89, 12],
    [592, 9, 79],
    [4, 812, 15],
    [142, 1, 76],
    [5, 89, 79],
    [4, 12, 598],
    [8, 79, 4],
]
my_list = [5, 89, 12, 592, 9, 79]
result = split_list_into_equal_sublists(my_list)
print(result)
assert result == [[5, 89], [12, 592], [9, 79]]
