file = open("dane/liczby.txt", "r")
dane = file.read().splitlines()
ile = 0
for wiersz in dane:
    if wiersz[len(wiersz) - 1] == '2':
        if wiersz[len(wiersz) - 2] == '0':
            ile += 1
print(ile)
