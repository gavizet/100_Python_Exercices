# 12. Demander à l'utilisateur un âge et afficher s'il est un enfant (moins de 12 ans), un adolescent (entre 12 et 18 ans) ou un adulte (plus de 18 ans). 

def what_is_user_age(my_input: str):
    try:
        age = int(input(my_input))
    except:
        raise TypeError("Bruh")
    if age >= 0 and age < 12:
        print("Hey kiddo, want a cookie ?")
    elif age >= 12 and age <= 18:
        print("You like that acnea ?")
    elif age > 18:
        print("Big boy, aren't we ?")
    else:
        what_is_user_age("Age needs to be a positive number: ")

what_is_user_age("What is your age ? ")