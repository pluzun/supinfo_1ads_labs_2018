
def histogramme(dic):
    sum_values = 0
    for value in dic.values():
        sum_values += value

    for key, value in dic.items():
        percent = (value / sum_values) * 100
        percent_rounded = "%.2f" % round(percent, 2)
        print("{key} : {percent}% ".format(key=key, percent=percent_rounded) + "*" * int(percent))

dic = {'a': 3, 'b': 4, 'c': 8, 'd': 5}
histogramme(dic)
