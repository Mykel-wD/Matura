file = open("dane_PR/liczby.txt", "r")
dane = file.read().splitlines()

def konwersja(binarna):
    binarna = binarna[::-1]
    potega = 0
    suma = 0
    for znak in binarna:
        suma += int(znak) * 2**potega
        potega += 1
    return suma
dwa = 0
osiem = 0
for wiersz in dane:
    liczba = konwersja(wiersz)
    if liczba % 2 == 0:
        dwa += 1
    if liczba % 8 == 0:
        osiem += 1
print(dwa)
print(osiem)
