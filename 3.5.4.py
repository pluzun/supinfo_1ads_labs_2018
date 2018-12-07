romain = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def convert(number):
    sum = 0
    for i in range(len(number)):
        value = romain[number[i]]
        if i + 1 < len(number) and romain[number[i + 1]] > value:
            sum -= value
        else:
            sum += value

    return sum


number = 'XCI'
print(convert(number))
