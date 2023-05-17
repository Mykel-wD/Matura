file = open("galerie.txt", 'r')
dane = file.read().splitlines()

m2 = []
for wiersz in dane:
    w = wiersz.split(" ")
    p = w[2:len(w)]
    m = w[1]
    ile = 0
    suma = 0
    for i in range(0,len(p),2):
        if p[i] != '0':
            ile += 1
            suma += int(p[i])*int(p[i+1])
    print(m,"powierzchnia",suma, " lokali",ile)
    m2.append(suma)
maxpow = max(m2)
minpow = min(m2)
d1 = dane[m2.index(maxpow)]
d2 = dane[m2.index(minpow)]
print("max ",d1.split(" ")[1],maxpow)
print("min ",d2.split(" ")[1],minpow)
