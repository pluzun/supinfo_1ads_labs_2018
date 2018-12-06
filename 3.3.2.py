# def selection(l):
#     l2=[]
#     for i in range(len(l)):
#         l2.append(min(l))
#         l.remove(min(l))
#     l=l2[:]
#     print(l)

def sorted(list_0):
    for i in range(len(list_0) - 1):
        if list_0[i] > list_0[i + 1]:
            return False

    return True

def selection(list_0):
    index = 0
    mini_index = index
    mini = list_0[mini_index]

    while not sorted(list_0):
        for i in range(index, len(list_0)):
            if list_0[i] < mini:
                mini_index = i
                mini = list_0[mini_index]

        list_0[index], list_0[mini_index] = mini, list_0[index]

        index += 1
        mini_index = index
        mini = list_0[mini_index]

    return list_0

l=[5,8,6,7,3,4,9,1,2]
print(selection(l))
