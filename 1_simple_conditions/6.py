# 6. Écrire un programme qui compare deux nombres et affiche le plus grand.

def biggest_number(number_pair) -> list:
    if number_pair[0] == number_pair[1]:
        return None
    elif number_pair[0] > number_pair[1]:
        return number_pair[0], number_pair[1]
    return [number_pair[1], number_pair[0]]

numbers_lists = [[1, 2],
        [0, 9],
        [10, 11],
        [0, 0]]
for num_pair in numbers_lists:
    res = biggest_number(num_pair)
    if res:
        print(f"{res[0]} > {res[1]}")
    else:
        print(f"{num_pair[0]} == {num_pair[1]}")