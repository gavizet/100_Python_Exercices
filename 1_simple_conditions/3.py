# 3. Créer un programme qui affiche "Vous êtes mineur" si l’âge est inférieur à 18.

def is_an_adult(age):
    if age < 18:
        return "vous etes mineur"
    return "vous etes majeur"

ages= [8, 18, 28]
for age in ages:
    print(f"Vous avez {age} ans, {is_an_adult(age)}")