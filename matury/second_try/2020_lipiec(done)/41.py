file = open("dane/identyfikator.txt", 'r')
dane = file.read().splitlines()


def suma(a):
    s = 0
    for cyfra in a:
        s += int(cyfra)
    return s


ids = []
for wiersz in dane:
    n = suma(wiersz[3:9])
    ids.append(n)
idm = max(ids)
for wiersz in dane:
    if suma(wiersz[3:9]) == idm:
        print(wiersz)

