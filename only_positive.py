#adjuk össze a pozitív számokat csak



numbers = [23, 54, 0, 76, -10, 0, 54, -21, -35, 0, 10]
sum = 0
for n in numbers:
    if n > 0:
        sum += n
print(sum)    

#számolja meg és írja ki hogy hány 0 szerepel

numbers = [23, 54, 0, 76, -10, 0, 54, -21, -35, 0, 10]
count = 0
for n in numbers:
    if n == 0:
        count += 1
print(count)