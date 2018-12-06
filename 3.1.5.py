a = [1,2,3,4,5]
n = 6
def liste(a, i, n):
    if a[i] == n:
        return i

    if i == len(a) - 1:
        return -1

    return liste(a, i + 1, n)

print(liste(a, 0, n))
