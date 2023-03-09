import math

file = open("Dane_NOWA/punkty.txt", 'r')
dane = file.read().splitlines()
zapis = open("zapis.txt", "w")
zapis.write("")
zapis = open("zapis.txt", 'a')
file.close()

srodek = 0
a = 200
b = 200
r = 200
r2 = r * r
# nk*P = n*Pk /:n
# nk*P/n = pi*r2 /:r2
# nk*P/n/r2 = pi

for n in range(1,1701):
    punkt = dane[n].split(" ")
    x = int(punkt[0])
    y = int(punkt[1])
    if (x - a) ** 2 + (y - b) ** 2 == r ** 2:
        srodek += 1
    elif (x - a) ** 2 + (y - b) ** 2 < r ** 2:
        srodek += 1
    nk = srodek
    P = 400 * 400
    pi = round(((nk * P) / n) / r2, 4)
    print(pi)
    blad = round(abs(math.pi - pi), 4)
    linia = str(blad) + "\n";
    zapis.write(linia)
zapis.close()
