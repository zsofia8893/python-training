if True:
    print("Ez mindig lefut")

if False:
    print("Ez sosem fog lefutni")    

if 5 > 10:
    print("nem fog lefutni, mert false")   

n = 10
n % 2 == 0 #páros
n %2 == 1 #páratlan

number = int(input("Adj meg egy számot: "))

if number % 2 == 0:
    print("páros")
if number % 2 != 0:
    print("páratlan")