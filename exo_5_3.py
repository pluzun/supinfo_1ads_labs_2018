def exist(my_list, element):
    print('Recursive')
    if len(my_list) == 1:
        return my_list[0] == element

    size = len(my_list)
    mid = size // 2

    x = exist(my_list[:mid], element)
    y = exist(my_list[mid:], element)

    return x or y

my_list = [i for i in range(1000000)]
print(exist(my_list, 5540))
