#string egy adatszerkezet, hiszen karakterekből áll
name = "John Doe"
for c in name:  #végig megy a karaktereken
    print(c)

count = 0
for c in name:
    if c == "o":
        count +=1  #mindig ad hozzá egyet, így adja össze az 'o' betűket
print(count)

print(name[3])   #3. karaktert írja ki az 'name'-ből itt a John 0-val kezd

#szeletelés, slicing
print(name[1:4])

print(len(name))

print("John" in "John Doe")

if "John" in name:
    print("Na még egy John")

#stringeknek vannak saját függvényei: metódusok    stringen kell meghívni / name változón hívjuk meg (ezért nincs semmi a zárójelben)

print(name.upper())

fruit = "            apple     "
print(fruit.strip())
