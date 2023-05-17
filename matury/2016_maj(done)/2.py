import math

file = open("dane/punkty.txt", "r")
dane = file.read().splitlines()

nk = 0
r = 200
for n in range(1, 1701):
    for wiersz in dane[0:n]:
        coords = wiersz.split(" ")
        x = int(coords[0])
        y = int(coords[1])
        od_srodka = math.sqrt((200 - x) ** 2 + (200 - y) ** 2)
        if od_srodka <= 200:
            nk += 1
    pk = nk * 160000 / n
    pin = round(pk / r ** 2, 4)
    blad = round(abs(math.pi - pin), 4)
    zapis = open("zapis.txt", "a")
    linia = str(n)+" "+str(blad)+"\n"
    zapis.write(linia)
    nk = 0
