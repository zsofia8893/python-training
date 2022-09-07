#szimuláljuk a dobókocka dobást

from random import randint, sample, shuffle
from secrets import choice

# randint függvény nem built-in function, hanem a standard libary része
number = randint(1, 6)
print(number)


numbers = [2, 4, 6, 8]
shuffle(numbers)
print(numbers)

cards = ["alsó", "felső", "király", "ász"]
card = choice(cards)
print(card)

print(sample(cards, k=2))