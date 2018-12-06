def fast_sort(list_0):
    if list_0 == []:
        return list_0

    pivot = list_0.pop(0)
    list_1 = []
    list_2 = []

    for i in list_0:
        if i < pivot:
            list_1.append(i)
        else:
            list_2.append(i)

    return fast_sort(list_1) + [pivot] + fast_sort(list_2)


list_0 = [1, 5, 4, 0, 3, 10]
print(fast_sort(list_0))

# def fast_sort(liste):
#     if not liste:
#         return []
#     else:
#         pivot = liste[-1]
#         petit = [x for x in liste if x < pivot]
#         grand = [x for x in liste[:-1] if x >= pivot]
#         return fast_sort(petit) + [pivot] + fast_sort(grand)
# liste = [1, 5, 4, 0, 3, 10]
# print(fast_sort(liste))
