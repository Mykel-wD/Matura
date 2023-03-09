file = open("dane/dane_6_3.txt", "r")
dane = file.read().splitlines()


def deszyfr(slowo1, slowo2):
    z1 = ord(slowo1[0])
    z2 = ord(slowo2[0])
    if z1 > z2:
        klucz = z1 - z2
        ile = -1
    else:
        klucz = z2 - z1
        ile = 1
    for znak in range(len(slowo1)):
        k = ord(slowo1[znak])
        drugi = ord(slowo2[znak])
        for dlugosc in range(klucz):
            if z1 > z2:
                if k <= 65:
                    k = 90
                else:
                    k += ile
            elif z2 > z1:
                if k >= 90:
                    k = 65
                else:
                    k += ile

        if k != ord(slowo2[znak]):
            return True
    return False

for wiersz in dane:
    w = wiersz.split(" ")
    wyraz1 = w[0]
    wyraz2 = w[1]
    if deszyfr(wyraz1, wyraz2):
        print(wiersz)
