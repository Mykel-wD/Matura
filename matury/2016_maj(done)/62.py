odczyt = open("dane_nowa/dane_6_2.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()
zapis = open("wyniki_6_2.txt", "a")
tekst = ""

for wiersz in dane:
    slowo = ""
    kod_k = wiersz.split(" ")
    szyfr = kod_k[0]
    if kod_k[1] == '':
        tekst = szyfr + "\n"
        zapis.write(tekst)
    else:
        k = int(kod_k[1])
        for znak in szyfr:
            cyfra = ord(znak)
            for i in range(k):
                if cyfra == 65:
                    cyfra = 90
                else:
                    cyfra -= 1
            slowo += chr(cyfra)
        tekst = slowo+"\n"
        zapis.write(tekst)
