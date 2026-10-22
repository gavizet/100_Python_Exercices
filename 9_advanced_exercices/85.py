"""
85. Créer une boucle qui simule un lancer de dés jusqu'à obtenir un 6.
"""

from random import randint

random_num = -1
while random_num != 6:
    input("Press enter to roll the dice. I will stop if I get a 6.")
    random_num = randint(1, 6)
    if random_num == 6:
        print("Got a 6, congrats. Now fuck off kindly.")
    else:
        print(f"Unlucky, got a {random_num}, we keep going")
