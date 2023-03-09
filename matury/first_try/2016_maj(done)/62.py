import math

file = open("dane/dane_6_2.txt", "r")
dane = file.read().splitlines()


def deszyfr(slowo, k):
    roz = ""
    for znak in slowo:
        l = ord(znak)
        for klucz in range(1, k + 1):
            if l <= 65:
                l = 90
            else:
                l -= 1
        z = chr(l)
        roz += z
    return roz


for wiersz in dane:
    spacja = False
    if wiersz[len(wiersz) - 1] == " ":
        spacja = True
    if spacja:
        print(wiersz)
        continue
    else:
        w = wiersz.split(" ")
        wyraz = w[0]
        kluczyk = int(w[1])
        print(deszyfr(wyraz, kluczyk))
