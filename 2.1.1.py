prix_unitaire = int(input("Entrer le prix : "))
tva = int(input("Entrer la TVA (%) : "))
nombre_article = int(input("Entrer le nombre d'articles : "))

# Calcul TVA
tva /= 100
tva += 1

prix_total = prix_unitaire * tva * nombre_article

print("Prix total : ", prix_total)
