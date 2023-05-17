import math

file = open("dane/dane_6_1.txt", "r")
dane = file.read().splitlines()

def szyfr(slowo, k):
    roz = ""
    for znak in slowo:
        l = ord(znak)
        for klucz in range(1,k+1):
            if l >= 90:
                l = 65
            else:
                l += 1
        z = chr(l)
        roz += z
    return roz
for wiersz in dane:
    print(szyfr(wiersz, 107))





