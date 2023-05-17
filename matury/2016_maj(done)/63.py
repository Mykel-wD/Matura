odczyt = open("dane_nowa/dane_6_3.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()
zapis = open("wyniki_6_3.txt", "a")
tekst = ""

for wiersz in dane:
    kod_k = wiersz.split(" ")
    szyfr = kod_k[1]
    slowo = kod_k[0]
    k = 0
    c1 = ord(slowo[0])
    c2 = ord(szyfr[0])
    while c1 != c2:
        if c1 == 90:
            c1 = 65
        else:
            c1 += 1
        k += 1
    for znak in range(len(slowo)):
        cyfra = ord(slowo[znak])
        for ii in range(k):
            if cyfra == 90:
                cyfra = 65
            else:
                cyfra += 1
        t1 = chr(cyfra)
        t2 = szyfr[znak]
        if chr(cyfra) != szyfr[znak]:
            tekst = slowo + "\n"
            zapis.write(tekst)
            break
