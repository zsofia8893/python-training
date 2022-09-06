#kérj be egy egész számot és írj ki az összes egész párosszámot
#pl 8; legyen 2,4,6,8


typednumber = int(input("Írj be egy számot:"))
print(typednumber)
for i in range(2,typednumber + 1, 2):  #start number, end number, hanyasával lépe felfele
    print(i)