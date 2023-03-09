file = open("dane/liczby.txt", "r")
dane = file.read().splitlines()
ile = 0
for wiersz in dane:
    if wiersz[len(wiersz)-1] == '8':
        ile += 1
print(ile)