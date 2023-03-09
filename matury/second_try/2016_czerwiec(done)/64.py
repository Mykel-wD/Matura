odczyt = open("dane/liczby.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()

def na_d(n):
    suma = 0
    base = int(n[len(n)-1:len(n)])
    n = n[0:len(n)-1]
    n = n[::-1]
    potega = 0
    for znak in n:
        suma += int(znak)*base**potega
        potega += 1
    return suma

liczba = 0
for wiersz in dane:
    if wiersz[len(wiersz)-1] == '8':
        liczba += na_d(wiersz)
print(liczba)