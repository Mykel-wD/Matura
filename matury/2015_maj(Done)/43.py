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
liczby = []
for wiersz in dane:
    liczba = konwersja(wiersz)
    liczby.append(liczba)
maks = max(liczby)
mini = min(liczby)
print("max: ", liczby.index(maks)+1)
print("min: ", liczby.index(mini)+1)

