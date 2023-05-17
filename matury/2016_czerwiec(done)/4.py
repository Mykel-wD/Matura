file = open("dane/liczby.txt", "r")
dane = file.read().splitlines()
ile = 0

def convert(liczba):
    liczba = liczba[::-1]
    baza = 8
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i]) * baza**i
    return  suma

for wiersz in dane:
    if wiersz[len(wiersz) - 1] == '8':
        kod = wiersz[0:len(wiersz) - 1]
        ile += convert(kod)
print(ile)
