#függvények több paraméterrel
from stringprep import c22_specials


def print_name_times(name, c):
    for i in range(c):  #range egész számot tud értelmezni
        print(name)


print_name_times("Joe", 5)

#írj egy print_sum nevű függvényt, mely vár egy i és j paramétert és kiírja az i és a j összegét
#hívd meg (5,10) és (8,3)

def print_sum(i,j):
    print(j + i)
    
print_sum(5, 10)
print_sum(8, 3)
