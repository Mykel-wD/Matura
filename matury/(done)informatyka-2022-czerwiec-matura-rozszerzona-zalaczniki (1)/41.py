file = open("dane/liczby.txt", 'r')
dane = file.read().splitlines()
rozne = []
liczbki = {}
for wiersz in dane:
    if wiersz not in rozne:
        rozne.append(wiersz)
    if wiersz in liczbki.keys():
        liczbki[wiersz] += 1
    else:
        liczbki[wiersz] = 1
print(len(rozne))
dwa = 0
trzy = 0
for l in liczbki.values():
    if l == 2:
        dwa += 1
    if l == 3:
        trzy += 1
print(dwa)
print(trzy)