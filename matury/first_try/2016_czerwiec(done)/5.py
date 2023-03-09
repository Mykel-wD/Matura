file = open("dane/liczby.txt", "r")
dane = file.read().splitlines()
min_liczba = 999999
max_liczba = 0


def convert(liczba, baza):
    liczba = liczba[::-1]
    suma = 0
    for i in range(len(liczba)):
        suma += int(liczba[i]) * baza ** i
    return suma


for wiersz in dane:
    kod = wiersz[0:len(wiersz) - 1]
    podstawa = int(wiersz[len(wiersz) - 1])
    wartosc = convert(kod, podstawa)
    if wartosc < min_liczba:
        min_liczba = wartosc
        min_kod = wiersz
    if wartosc > max_liczba:
        max_liczba = wartosc
        max_kod = wiersz
print(max_kod, max_liczba)
print(min_kod, min_liczba)
