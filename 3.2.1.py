x = int(input("Enter a real number : "))
n = int(input("Enter the puissance of x : "))

def exponentiation(x, n):
    if n == 0 or x == 1:
        return 1
    elif x == 0:
        return x

    if n % 2 == 0:
        return exponentiation(x**2, n//2)
    else:
        return x * exponentiation(x**2, (n-1)//2)

print(exponentiation(x, n))
