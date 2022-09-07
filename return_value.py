# van visszatérési értéke; int(), input(), str(), range(), len().
#nincs visszatérési értéke; print()
#ha a szám kisebb, mint 0, akkor -1-et adjon vissza
#ha 0, akkor 0-át adjon vissza
#ha nagyobb, mint 0 akkor 1-et adjon vissza

def if_bigger_0(n):
    if n > 0:
        return -1
    elif n == 0:
        return 0
    else:
        return 1

print(if_bigger_0(1))
print(if_bigger_0(-1))

