file = open("dane_PR/dziennik.txt", 'r')
dane = file.read().splitlines()
ciag = 1
pierszy = 0
ostatni = 0
dlugosc = 0
for wiersz in range(1,len(dane)):
    info = dane[wiersz]
    if int(dane[wiersz]) > int(dane[wiersz - 1]):
        ciag += 1
    else:
        if ciag > dlugosc:
            pierszy = int(dane[wiersz - ciag])
            ostatni = int(dane[wiersz - 1])
            lepszy = ostatni - pierszy
            dlugosc = ciag
        ciag = 1
print(dlugosc, " ", lepszy)
