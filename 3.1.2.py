def syracuse(a, n):
    if n == 0:
        return a

    print(int(a))
    if a % 2 == 0:
        return syracuse(a/2, n-1)
    else:
        return syracuse(a*3+1, n-1)

a = int(input("a : "))
n = int(input("n : "))
print(int(syracuse(a, n-1)))
