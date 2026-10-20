'''
65. Parcourir un dictionnaire et afficher ses clés et valeurs. 
my_dict = { 
    'nom': 'Alice', 
    'age': 25, 
    'ville': 'Paris', 
    'profession': 'Développeuse', 
    'langages': ['Python', 'JavaScript', 'C++'] 
} 
'''

my_dict = { 
    'nom': 'Alice', 
    'age': 25, 
    'ville': 'Paris', 
    'profession': 'Développeuse', 
    'langages': ['Python', 'JavaScript', 'C++'] 
} 

for key, value in my_dict.items():
    print(f"{key}: {value}")