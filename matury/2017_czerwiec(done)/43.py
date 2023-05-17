import math

file = open("dane/punkty.txt", 'r')
dane = file.read().splitlines()


odleglosci = []
punkty = []

for kord in dane:
    x = int(kord.split(" ")[0])
    y = int(kord.split(" ")[1])
    for kord2 in dane:
        if kord != kord2:
            x2 = int(kord2.split(" ")[0])
            y2 = int(kord2.split(" ")[1])
            odl = (x2-x)**2 + (y2-y)**2
            odl = math.sqrt(odl)
            odleglosci.append(round(odl,0))
            punkty.append([kord, kord2])
odl = max(odleglosci)
nr = odleglosci.index(odl)
print(punkty[nr], odleglosci[nr])