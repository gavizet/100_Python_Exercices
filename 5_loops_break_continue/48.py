# 48. Utiliser continue pour ignorer les lettres 'a' et 'e' lors de l'affichage des lettres d'un mot. 


word_list = ["test", "coucou", "gaga", "gaetan", ""]
for word in word_list:
    result_word = []
    for char in word:
        if char == 'a' or char == 'e':
            continue
        result_word.append(char)
    print(f"Starting Word: {word} | Result: {result_word}")
