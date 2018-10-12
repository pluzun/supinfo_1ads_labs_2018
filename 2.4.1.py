n = int(input("Donner un nbr : "))

def fibonacci(n=10):
    if n < 2:
        return n
    else:
        a = 0
        b = 1
        number = 0

        for i in range(2, n + 1):
            number = a + b
            a = b
            b = number

        return number

print(fibonacci(n))
