n = int(input("n premier terme = "))
def nPremierCube(n):
    if n <= 1:
        return n
    return n**3 + nPremierCube(n-1)
print(nPremierCube(n))
