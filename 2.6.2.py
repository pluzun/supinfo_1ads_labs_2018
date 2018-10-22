def presence(liste, number):
    return liste.index(number) if number in liste else -1

liste = [0, 1, 2, 3, 4, 5, 6, 7]
number = int(input("éléments recherché :"))
print(presence(liste, number))
