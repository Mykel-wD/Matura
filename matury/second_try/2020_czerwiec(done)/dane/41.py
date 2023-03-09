file = open("pary.txt", 'r')
dane = file.read().splitlines()
"""
Tablica z pierszymi
"""
pierwsze = []


def pierwsza(n):
    for dz in range(2, n):
        if n % dz == 0:
            return False
    return True


for i in range(2, 100):
    if pierwsza(i) and i % 2 == 1:
        pierwsze.append(i)
print(dane)
"""
Tablica z pierszymi
"""
for wiersz in dane:
    liczba = int(wiersz.split(" ")[0])
    if liczba > 4 and liczba % 2 == 0:
        pot = []
        roznice = []
        for p1 in pierwsze:
            for p2 in pierwsze:
                if p1 + p2 == liczba:
                    pot.append([p1, p2])
                    roznice.append(abs(p1 - p2))
        w = pot[roznice.index(max(roznice))]
        print(liczba, w[0], w[1])
