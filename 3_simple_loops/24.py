# 24. Demander à l'utilisateur un nombre de 1 à 10 et afficher la table de multiplication.

def print_multi_table(num: int) -> None:
    if num >= 1 and num <= 10:
        for i in range(1, num + 1):
            print(f"{num} * {i} = {num * 1}")
    else:
        print("I said a number between 1 and 10 you dimwit")

try:
    num_to_multiply = int(input("Give me a number between 1 and 10, I will write down its multiplication table: "))
    print_multi_table(num_to_multiply)
except:
    print("Bro, that's not even an int")