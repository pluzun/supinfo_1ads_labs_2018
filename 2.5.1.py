n = int(input("Entrer une borne : "))

def estParfait(n):
    diviseurs = 0
    for i in range(1, n):
        if n%i == 0:
            diviseurs += i
    return diviseurs == n

for i in range(1, n + 1):
    if estParfait(i):
        print(i)
