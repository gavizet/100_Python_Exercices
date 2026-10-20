'''
53. Utiliser des boucles imbriquées pour afficher une pyramide de nombres. 
'''

# Using List Comprehension
def print_pyramid_1() -> None:
    print("Inversed pyramid using list comprehension\n")
    pyramid_size = int(input("Give my a size, I will print a pyramid: "))
    if pyramid_size <= 0:
        raise ValueError("Need a positive number")
    for index in range(1, pyramid_size+1, 1):
        spaces = (index - 1) * "  "
        num_row = list(range(1, pyramid_size, 1)) + list(range(pyramid_size, 0, -1))
        print(spaces, end="")
        print(*num_row, end="")
        print(spaces)
        pyramid_size -= 1

# Using nested loops
def print_pyramid_2() -> None:
    print("\nPyramid using nested loops")
    try:
        pyramid_size = int(input("Give my a size, I will print a pyramid: "))
        if pyramid_size <= 0:
            raise ValueError("Need a positive number")
        for i in range(0, pyramid_size+1, 1):
            spaces = pyramid_size * "  "
            print(spaces, end="")
            for j in range(1, i, 1):
                print(j, end=" ")
            for j in range(i, 0, -1):
                print(j, end=" ")
            print(spaces)
            pyramid_size -= 1
    except:
        print("That's not a number")

print_pyramid_1()
print_pyramid_2()
