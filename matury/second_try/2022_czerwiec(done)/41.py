file = open("dane/liczby.txt", "r")
dane = file.read().splitlines()
file.close()

dwa = 0
trzy = 0
szyskie = []
rozne = []
for n in dane:
    szyskie.append(n)
    if n not in rozne:
        rozne.append(n)
for r in rozne:
    if szyskie.count(r) == 2:
        dwa += 1
    if szyskie.count(r) == 3:
        trzy += 1
print("a", len(rozne))
print("b", dwa)
print("c", trzy )