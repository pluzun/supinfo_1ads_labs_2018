premier = int(input("Premier nombre : "))
deuxieme = int(input("Deuxieme nombre : "))
somme = premier

for _ in range(1, deuxieme):
    somme += premier

print(somme)
