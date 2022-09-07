n = 23
if n % 2 == 0:
    print("páros")       #igaz esetén ezt futtatja le
else:                    #különben / egyéb estben ezt írt ki;
    print("páratlan")

n = 24
if n > 0:
    print("pozitív")
elif n == 0:          #vagy ha; amikor az if false, ide került, innen ha false megy az else-re
    print("nulla")
else:
    print("negatív") 

    #írd ki az n szám abszolút értékét

n = int(input("szám:"))
if n >= 0:
    print(n)
else:
    print(-n)

# legyen két szám (i és j) és írd ki közülük a kisebbet
i = 10
j = 6
if i > j:
    print(j)
elif j > i:
    print(i)