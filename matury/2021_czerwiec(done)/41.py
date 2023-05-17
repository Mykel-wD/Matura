file = open("dane/napisy.txt", 'r')
dane = file.read().splitlines()
ile = 0
for wiersz in dane:
    for znak in wiersz:
       if ord(znak) < 65:
           ile += 1
print(ile)