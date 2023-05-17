odczyt = open("dane/liczby.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()


def na_d(n):
    suma = 0
    base = int(n[len(n) - 1:len(n)])
    n = n[0:len(n) - 1]
    n = n[::-1]
    potega = 0
    for znak in n:
        suma += int(znak) * base ** potega
        potega += 1
    return suma


liczby = []
for wiersz in dane:
    liczby.append(na_d(wiersz))
l_max = max(liczby)
i_max = liczby.index(l_max)
l_min = min(liczby)
i_min = liczby.index(l_min)
print("max: ", dane[i_max], " ", l_max)
print("min: ", dane[i_min], " ", l_min)
