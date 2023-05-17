file = open('dane_2105/instrukcje.txt', 'r')
dane = file.read().splitlines()

napis = []
for wiersz in dane:
    ins = wiersz.split(" ")[0]
    litera = wiersz.split(" ")[1]
    if ins == "DOPISZ":
        napis.append(litera)
    elif ins == "ZMIEN":
        if len(napis) > 0:
            napis[len(napis) - 1] = litera
    elif ins == "PRZESUN":
        if litera in napis:
            ind = napis.index(litera)
            if napis[ind] == 'Z':
                napis[ind] = 'A'
            else:
                napis[ind] = chr(ord(napis[ind]) + 1)
    elif ins == "USUN":
        if len(napis) > 0:
            napis.pop()
h = ''
for n in napis:
    h+=n
print(h)
