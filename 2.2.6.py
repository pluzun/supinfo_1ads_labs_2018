basse = int(input("Borne basse : "))
haute = int(input("Borne haute : "))

basse = basse + 1 if basse % 2 == 1 else basse + 2

for i in range(basse, haute, 2):
    print(i)
