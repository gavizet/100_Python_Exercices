'''
56. Utiliser des boucles imbriquées pour calculer et afficher le produit scalaire de deux vecteurs. 
vector_0 = [5, 89, 79, 4, 56] 
vector_1 = [8, 9.4, 12, 78, 7.7]
'''

vector_0 = [5, 89, 79, 4, 56] 
vector_1 = [8, 9.4, 12, 78, 7.7]

dot_product = 0
for i in range(len(vector_0)):
    dot_product += vector_0[i] * vector_1[i]
print(dot_product)

