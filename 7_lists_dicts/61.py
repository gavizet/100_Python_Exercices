'''
61. Utiliser une boucle pour inverser une liste. 
elements = [8, 9, 'mrt', 97, True, 1.2]
'''

print("Using negative slicing and print")
elements = [8, 9, 'mrt', 97, True, 1.2]
print(elements[::-1])

# OR
print("Using negative slicing and append")
new_list = []
for elem in elements[::-1]:
    new_list.append(elem)
print(new_list)

# OR
print("Using range()")
newer_list = []
for elem in range(len(elements) -1, -1, -1):
    newer_list.append(elements[elem])
print(newer_list)