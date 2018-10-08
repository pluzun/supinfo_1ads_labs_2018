a = int(input("Enter a :"))
b = int(input("Enter b :"))

if (a < 0 and b > 0) or (b < 0 and a > 0):
    print("Negatif")
elif a == 0 or b == 0:
    print("Nul")
else:
    print("Positif")
