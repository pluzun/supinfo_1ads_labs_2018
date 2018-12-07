def anagrammes(word):
    if len(word) == 1:
        return [word]
    elif len(word) == 2:
        return set([word, word[1] + word[0]])
    else:
        return set([word[i] + letter for i in range(len(word)) for letter in anagrammes(word[:i] + word[i + 1:])])

word = 'hel'
for element in anagrammes(word):
    print(element)
