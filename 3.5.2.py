liste = [80, 99, 20, 53, 59, 15, 81, 40, 52, 24, 20, 42, 15, 5, 87, 23, 25, 9, 82, 11]

def numberList(liste):
    dic = {x:0 for x in range(1,10)}
    for i in liste:
        dic[int(str(i)[0])] += 1
    return dic
print(numberList(liste))
