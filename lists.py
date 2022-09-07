names = ["Joe", "Jack", "Jane"]

for name in names:  #a lista lesz a range. #végig literálunk a names változó elemein
    print(name)

    #enumerate függvényt kell használni, ha az indexhez hozzá akarok férni

counter = 1
for name in names:
    print(counter)
    print(name)
    counter +=1

#Írd ki az első 3 hónap nevét egymás alá
months = ["january", "february", "march"]
for month in months:
    print(month)

#Írd ki hogy 'az év egyik hónapja' janár, az első 3 hónappal
for month in months:
    print("Az év egyik hónapja " + month)
    print(f"Az év egyi hónapja {month}.")


#Hozz létre egy listát a 3,7,9,13 számokkal! és add össze őket

numbers = [3, 7, 9, 13]
sum = 0
for number in numbers:
    sum += number 
    print(sum)
numbers = [3, 7, 9, 13]

sum = 0 # 0

number = 3

sum += number # 0 + 3 = 3

number = 7

sum += number # 3 + 7 = 10

number = 9

sum += number # 10 + 9 = 19

number = 13

sum += number # 19 + 13 = 32

print(sum)