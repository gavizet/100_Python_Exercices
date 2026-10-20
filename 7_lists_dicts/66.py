'''
66. Utiliser une boucle pour compter le nombre de voyelles dans une chaîne de 
caractères. 
'''
vowel_count = 0
string = input("Write any string, I will count the amount of vowels: ")
for char in string:
    if char in 'aeiouAEIOU':
        vowel_count += 1
print(f"There are {vowel_count} vowels in '{string}'")
