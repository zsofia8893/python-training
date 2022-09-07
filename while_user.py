#A felhasználótól kérj be egy számot és írd ki a kétszeresét
# egészen addig amíg 
number = int(input("Írj be egy számot:"))
while number > 0: #  '!='  nem egyenlőt jelent
    print(number * 2)
    number = int(input("Írj be egy számot: "))

szam = 100
while not szam == 0:
    szam = int(input("Adj meg egy számot:"))
    print(szam * 2)
