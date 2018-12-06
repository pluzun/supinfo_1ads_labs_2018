def fusion(list_1, list_2):
    if list_2 == []:
        return list_1
    elif list_1 == []:
        return list_2

    if list_1[0] < list_2[0]:
        return [list_1[0]] + fusion(list_1[1:], list_2)
    else:
        return [list_2[0]] + fusion(list_1, list_2[1:])


def tri_fusion(list_0):
    if len(list_0) <= 1:
        return list_0

    middle = len(list_0) // 2

    return fusion(tri_fusion(list_0[:middle]), tri_fusion(list_0[middle:]))


list_0 = [3, 5, 4, 6, 8, 2, 0, 1, 3, 2, 5, 14]
print(tri_fusion(list_0))
