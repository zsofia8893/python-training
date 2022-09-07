def print_hello_world():
    print("hello")
    print("world")

def print_hello_world_five_times():
    for i in range(0, 5):
        print_hello_world()

def print_hello(text):    #egy 1! paraméteres függvény  paraméter = argument
    print(f"hello {text}")
    #print(text)      #a parméter nem más mint egy változó   'text' itt a FORMÁLIS paraméter!!   a Joe az AKTUÁLIS paraméternek hívjuk

#beépített függvények: input(), print(), int(), str(), range(),
fruits = ["meggy", "cseresznye", "körte"]

#len()  hossz

print(len(fruits))  #lenght - hossz

print(len("hello world"))  # string hosszát adja vissza

#függvények: névvel ellátott utasítás csoport

#DRY: don't repeate yourself!!! Erre valók a függvények
#print("hello")
#print("world")

#print("hello")
#print("world")

print_hello_world() #előhívom a függvényt fentről, itt hajtja végre, ahol hivatkozok rá!
print_hello_world()

print_hello_world_five_times()

print("----")
print_hello("joe")

print_hello("Zsófi")