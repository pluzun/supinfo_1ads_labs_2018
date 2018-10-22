carre = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]

def calcul_coeff():
    coeff = 0

    for i in range(3):
        for j in range(3):
            coeff += carre[i][j]

    return coeff

def verif_coeff_ligne(carre, ligne, coeff):
    count = 0

    for i in range(3):
        count += carre[ligne][i]

    return coeff == count

def verif_coeff_colonne(carre, colonne, coeff):
    count = 0

    for i in range(3):
        count += carre[i][colonne]

    return coeff == count

def verif_coeff_diagonale(carre, diagonale, coeff):
    count = 0

    if diagonale == 0:
        for i in range(3):
            count += carre[i][i]
    else:
        for i in range(3):
            count += carre[i][2 - i]

    return coeff == count

def verif_carre_magique(carre):
    nb = calcul_coeff() / 3

    for i in range(3):
        if not verif_coeff_ligne(carre, i, nb):
            return False

        if not verif_coeff_colonne(carre, i, nb):
            return False

    for i in range(2):
        if not verif_coeff_diagonale(carre, i, nb):
            return False

    return True

print(verif_carre_magique(carre))
