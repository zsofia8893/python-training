#kérd be a felhasz nevét, hányszor kerüljön kiírásra
#Joe 3;
from collections import Counter


name=input("Mi a neved?")

count = int(input("Hányszor kerüljön kiírásra?"))  # str "10"  -> 10
print(name * count)

print((name + " ")*count)  #így tudsz space-t beletenni
