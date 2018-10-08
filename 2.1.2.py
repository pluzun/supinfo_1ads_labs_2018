old_x, old_y = int(input("x: ")), int(input("y: "))

# 1
print("1")
x, y = old_x, old_y
x, y = y, x
print("x: ", x, "\ny: ", y)

# 2
print("2")
x, y = old_x, old_y
z = y
y = x
x = z
print("x: ", x, "\ny: ", y)

# 3
print("3")
x, y = old_x, old_y
x += y
y = x - y
x -= y

print("x: ", x, "\ny: ", y)
