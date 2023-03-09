file = open("galerie_przyklad.txt", 'r')
dane = file.read().splitlines()

miasta = []
miasta_lokale = []
for wiersz in dane:
    w = wiersz.split(" ")
    lokale = w[2:len(w)]
    miasto = w[1]
    suma = 0
    rlokale = []
    for i in range(0,len(lokale),2):
        powierzchnia = int(lokale[i])*int(lokale[i+1])
        if powierzchnia not in rlokale and powierzchnia != 0:
            rlokale.append(powierzchnia)
    roznych = len(rlokale)
    miasta.append(miasto)
    miasta_lokale.append(roznych)
minl = min(miasta_lokale)
maxl = max(miasta_lokale)
print("min ",miasta[miasta_lokale.index(minl)], minl)
print("max ",miasta[miasta_lokale.index(maxl)],maxl)