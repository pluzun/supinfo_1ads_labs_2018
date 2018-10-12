mot_a = "logarighme"
mot_b = "algorithme"

def anagramme(mot_a, mot_b):
    if len(mot_a) != len(mot_b):
        return False

    for letter in mot_a:
        if mot_a.count(letter) != mot_b.count(letter):
            return False

    return True

print(anagramme(mot_a, mot_b))
