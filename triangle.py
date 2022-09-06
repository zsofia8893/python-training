base=20
height=10
print((base*height)/2)

base = int(input("Enter base:"))
height = int(input("Enter height:"))  #int kell hogy egész számként kezelje
area = base * height / 2

print(f"The area of triangle is {area}")  #f a {közötti részt kiértékelve} jeleníti meg

print(f"Érték: {1 + 3}")  #f nélkül csak annyi jelenik meg hogy  1 + 3

print(int(10))
print(int(10.7))  #levágyja a tizedespont utáni értéket az int függvény lebegőpontos számok esetén