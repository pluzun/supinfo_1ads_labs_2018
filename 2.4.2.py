a = int(input("base a: "))
n = int(input("n premiers termes de la suite de Syracus de base a: "))

def syracuse(a, n):
    for i in range(n):
        print(a)
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1

syracuse(a,n)
