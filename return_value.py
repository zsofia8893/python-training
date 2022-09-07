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


print("----")

# Írjatok egy függvényt, ami vár egy egész számot, és visszaadja
# annak abszolútértékét!

def absolut(c):
    if c < 0:
        result = -c
    else:
        result = c
    return result    #struktúrált programozás: minden függvényben CSAK egy return utasítás lehet.

print(absolut(-1))
print(absolut(2))



# Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
# visszaadja a területet!
def area(a, b):
    return a * b

print(area(3,2))


# Írjatok egy függvényt, mely várja a téglalap a és b oldalát, és
# visszaadja a kerületet!
def calculate_perimeter(a, b):
    return 2 * (a + b)

print(calculate_perimeter(4, 6))


# Írjatok egy függvényt, amely vár két számot, és visszaadja a
# kettő közül a nagyobbat!
def max(a, b):
    if a > b:
        return a
    else:
        return b

print(max(6, 9))
print(max(5, 3))


# Vár egy számot és visszaadja a "páros" szöveget, ha páros,
# ellenkező esetben hogy "páratlan"
def get_type(n):
    if n % 2 == 0:  # % csak a maradékos osztás, itt a maradéknak 0-nak kell lennie
        return "páros"
    else:
        return "páratlan"

print(get_type(6))
print(get_type(5))

#Ha a függvény boolean értéket ad vissza, akkor logikai függvény: True or False

#írj egy is_even nevű függvényt mely a paraméteréről eldönti hogy páros-e
#True ha páros, False ha páratlan

def is_even(n):
    if n % 2 == 0: #elosztjuk 2-vel ÉS a mardéka nulla
        return True
    else:
        return False

#EGYENŐ ezzel;

def is_even_simple(n):
    return n % 2 == 0

print(is_even(6))

print(is_even_simple(8))

if is_even(5):
    print("Ez egy páros szám!")
else:
    print("Ez egy páratlan szám!")

print(is_even(8))