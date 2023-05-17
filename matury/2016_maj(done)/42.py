import math

file = open("Dane_NOWA/punkty.txt", 'r')
dane = file.read().splitlines()
srodek = 0
a = 200
b = 200
r = 200
r2 = r*r
#nk*P = n*Pk /:n
#nk*P/n = pi*r2 /:r2
#nk*P/n/r2 = pi
n = len(dane)
for wiersz in range(n):
    punkt = dane[wiersz].split(" ")
    x = int(punkt[0])
    y = int(punkt[1])
    if (x - a) ** 2 + (y - b) ** 2 == r ** 2:
        srodek += 1
    elif (x - a) ** 2 + (y - b) ** 2 < r ** 2:
        srodek += 1
nk = srodek
P = 400*400
pi = round(((nk*P)/n)/r2,4)
print(pi)
blad = round(abs(math.pi - pi),4)
print(blad)