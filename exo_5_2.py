def max_list(my_list):
    if len(my_list) == 1:
        return my_list[0]

    size = len(my_list)
    mid = size // 2

    x = max_list(my_list[:mid])
    y = max_list(my_list[mid:])

    return x if x > y else y

my_list = [2, 5, 3, 4, 8]
print(max_list(my_list))
