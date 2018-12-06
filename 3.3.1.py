def tri_bulle(l):
    n = len(l) - 1
    for _ in range (n):
        for i in range(n):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
    return l

l = [28,8,54,5,2,12]
print(tri_bulle(l))
