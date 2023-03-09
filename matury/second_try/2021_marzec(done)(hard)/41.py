file = open("galerie.txt", 'r')
dane = file.read().splitlines()

panstwa = {}
for wiersz in dane:
    w = wiersz.split(" ")
    p = w[0]
    if p in panstwa.keys():
        panstwa[p] += 1
    else:
        panstwa[p] = 1
print(panstwa)

