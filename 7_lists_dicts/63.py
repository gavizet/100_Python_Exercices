'''
63. Créer une boucle qui compte le nombre de fois qu'un élément apparaît dans une liste. 
my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6] 
'''
def count_occurences(my_list: list, pattern) -> int:
    count = 0
    for val in my_list:
        if val == pattern:
            count += 1
    return count

my_list = [4, 2, 9, 12, 4, 32, 13, 8, 78, 1, 4, 21, 7, 4, 1, 3, 5, 4, 6]
pattern = 1
my_count = count_occurences(my_list, pattern)
assert my_count == my_list.count(pattern)
print(f"Found {pattern} occurs {my_count} times in {my_list}")
