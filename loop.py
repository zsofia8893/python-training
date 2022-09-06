#írd ki 5x egymás alá a nevünket (ciklussal)
import numbers
from unittest import result


print("István\n" * 5)

for i in range(5):  #ciklusváltozók általában; i, j, k, de lehet értelmes változót adni adj
    print(i)
    print("István")

# Feladat: Írj egy ciklust, ami kíírja a számokat 1-től 100-ig egymás alá!

for i in range(100):
    print(i + 1)

# Feladat: Írd ki egymás után a neved 5x, írd elé a sorszámot is!

for j in range(5):
    print(f"{j + 1}. Zsófi")


# Feladat: Írj egy ciklust, amely 1-től 10-ig kiíírja a számokat és azok négyzetét is egy új sorba!
for i in range(10):
    j = i + 1
    result = j **2
    print(f"A {j} szám négyzete: {result}")

    for i in range(5, 10):  #5,6,7,8,9 
        print(i)

# az i felveszi a következő értékeket: 5<= i <10
for i in range(10, 20, 2):
    print(i)

# lépé negatív szám, csökkenteni, estünkben 10től 1ig;
for i in range(10, 0, -1):
    print(i)

