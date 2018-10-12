# line = int(input("nombre de ligne"))
# while line != 0:
#     print("*"* line)
#     line -= 1

line = int(input("nombre de ligne"))
for i in range(line, 0, -1):
    print("*" * i)
