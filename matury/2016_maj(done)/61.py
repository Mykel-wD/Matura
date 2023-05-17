odczyt = open("dane_nowa/dane_6_1.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()
zapis = open("wyniki_6_1.txt", "w")

tekst = ""
for wiersz in dane:
    slowo = ""
    for znak in wiersz:
        cyfra = ord(znak)
        for k in range(107):
            if cyfra == 90:
                cyfra = 65
            else:
                cyfra += 1
        slowo += chr(cyfra)
    tekst = tekst + slowo+"\n"
zapis.write(tekst)
