L = [7,5,5,8,3,46,54,38,25]

def insertion(L):
    for i in range(1, len(L)):
        a = L[i]
        j = i - 1
        while L[j] > a and j >= 0:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = a
        
    return L

print(insertion(L))
