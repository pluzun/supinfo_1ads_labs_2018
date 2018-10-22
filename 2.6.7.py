q = [int(x) for x in input("inserer des chiffres :").split()]

def drapeau(q):
    q.sort()
    print(q)
    y = q.count(1)
    z = q.count(2)
    x = q.count(3)
    print(y,z,x)

drapeau(q)
