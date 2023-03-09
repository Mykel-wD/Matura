file = open("dane_PR/liczby.txt", "r")
dane = file.read().splitlines()

ile = 0
for wiersz in dane:
    if wiersz.count("0") > wiersz.count("1"):
        ile += 1
print(ile)