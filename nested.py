#ciklusk egymásba ágyazása
from unittest import result


for i in range(3):
    for j in range(5, 10):
        print(f"{i} - {j}")

# írd ki a 10es szorzótáblát

for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} * {j} = {result}")

# négyzet alakban a szorzótábla
line = "" #üres string, 0 karaktert tartalmazó string, 0 hosszú string
for i in range(1, 10):
    line += str(i) + " "
    print(line)

for i in range(1, 11):
    line = " "
    for j in range(1, 11):
        line += str(i * j) + " "
    print(line)

#ciklusban lehet elágazás is;
for i in range(1, 11):
    line = " "
    for j in range(1, 11):
        result = i * j
        if result < 10:
            line += str(i * j) + " "
    print(line)
