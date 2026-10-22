"""
87. Créer un programme qui génère un nombre aléatoire entre 1 et 100 et indique plus ou moins jusqu’à ce que l’utilisateur trouve.
"""

from random import randint

random_num = randint(1, 100)
print(random_num)
while random_num != 0:
    try:
        user_guess = int(input("Guess my number between 1 and 100: "))
        if user_guess > 100 or user_guess < 1:
            print("I said between 1 and 100 you dimwit")
        elif user_guess < random_num:
            print("Higher")
        elif user_guess > random_num:
            print("Lower")
        elif user_guess == random_num:
            print(f"You found it, it was {random_num}! See you later.")
            random_num = 0
    except:
        print("Not a number")
