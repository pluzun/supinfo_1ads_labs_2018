from string import ascii_lowercase

def getLetters(string):
    dic = {}

    for letter in string.lower():
        if letter in ascii_lowercase:
            dic[letter] = dic.setdefault(letter, 0) + 1

    return dic

def isPangramme(string):
    return len(getLetters(string)) == 26

print(getLetters("Portez ce vieux whisky au juge blond qui fume !"))
print(isPangramme("Portez ce vieux whisky au juge blond qui fume !"))

# testing_sentence = str(input("Taper la phrase à tester : "))
# d_occurence = {}
#
# def testing(testing_sentence):
#     for letters in testing_sentence.lower():
#         if letters in d_occurence:
#             d_occurence[letters] += 1
#         else:
#             if letters not in ascii_lowercase:
#                 continue
#             d_occurence.update({letters: 1})
#
#
# def pangramme(d_occurence):
#     if len(d_occurence) == 26:
#         return True
#     else:
#         return False
#
# testing(testing_sentence)
# print("Dictionnaire des occurences de : " + testing_sentence)
# print(d_occurence)
# if pangramme(d_occurence):
#     print("La phrase est un pangramme")
# else:
#     print("La phrase n'est pas un pangramme")
