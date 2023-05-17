file = open("Dane_NOWA/punkty.txt", 'r')
dane = file.read().splitlines()

srodek = 0
a = 200
b = 200
r = 200
for wiersz in dane:
    punkt = wiersz.split(" ")
    x = int(punkt[0])
    y = int(punkt[1])
    if (x-a)**2 + (y-b)**2 == r**2:
        srodek += 1
    elif (x-a)**2 + (y-b)**2 < r**2:
        srodek += 1

print("srodek: ", srodek)