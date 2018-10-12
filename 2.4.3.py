def comparaison(s):
    if first[s] != second[s]:
        return 1

    return 0

first, second = str(input("votre premier mot: ")), str(input("votre second mot: "))
score = 0

l_f = len(first)
for i in range(0, l_f):
    score += comparaison(i)

print(score)
