# logikai kifejezések

#logikai literál
True
False
print(type(True))

# És: Ha van tojás és van szalonna, akkor csináljunk ham&eggs-t

print(True and True)
print(True and False)


#Vagy: Ha éhes vagy vagy 16:00 óra múlt, akkor egyél

print(True or True)
print(True or False)
print(False or True)
print(False or False)


#Negáció: Az adott valaminek az ellenétét használja
print(not True)
print(not False)


#Kombiálva
print(((not True) or(False)) and (not False))

# Összehasonlítások: relációs jelek
print(1 < 2)
print(1 > 2)
print(1 == 2) #Vigyázz, összehasonlítás KÉT egyenlőség jel

print(1 < 5 < 10)

#Hogyan döntsük el egy számról, hogy pásors-e
print(9 % 2 == 0)  # % jel maradékos osztás!!!
#Ha számot osztjuk 2vel, és páros, ha a maradék nulla

#Kérjük be a felhasználótól egy számot és írjuk ki hogy False, ha páros és True ha a szám páratlan

szam = int(input("Írj be egy számot:"))
print(szam % 2 == 1)
print(not(szam % 2 == 0))



