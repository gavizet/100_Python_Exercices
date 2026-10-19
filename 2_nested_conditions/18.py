# 18. Écrire un programme qui affiche "Excellent" si la note est supérieure à 85, "Bien" si elle est entre 70 et 85, sinon afficher "Peut mieux faire".

def print_score(my_score: int) -> None:
    if my_score >= 70 and my_score <= 85:
        print("Bien")
    elif my_score < 70:
        print("Peut mieux faire")
    else:
        print("Excellent")

notes_list = [-12, 0, 70, 85, 86, 99, 102]
for note in notes_list:
    print_score(note)