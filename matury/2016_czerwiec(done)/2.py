file = open("dane/liczby.txt", "r")
dane = file.read().splitlines()
ile = 0
for wiersz in dane:
    dobra = True
    if wiersz[len(wiersz) - 1] == '4':
        for znak in wiersz:
            if znak == '0':
                dobra = False
        if dobra:
            ile += 1
print(ile)
