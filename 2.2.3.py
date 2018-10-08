x = int(input("Enter X: "))
y = int(input("Enter Y: "))
z = int(input("Enter Z: "))

if x < y and x < z:
    print(x, end=' ')
    print(y, z) if y < z else print(x, y)
if y < x and y < z:
    print(y, end=' ')
    print(x, z) if x < z else print(z, x)
if z < x and z < y:
    print(z, end=' ')
    print(x, y) if x < y else print(y, x)
