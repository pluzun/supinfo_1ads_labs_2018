lines=int(input("saisir un entier"))

# etoile=1
# for i in range(1,lines+1):
#     print((lines-i)*" "+"*"*etoile)
#     etoile+=2

for i in range(lines):
    print(((lines - i) * " ") + "*" * (i*2 + 1))
