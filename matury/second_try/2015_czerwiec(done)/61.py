file = open("dane/kody.txt")
dane = file.read().splitlines()
zapis = open("kody1.txt", "a")
for wiersz in dane:
    suma_p = 0
    suma_n = 0
    for cyfra in range(1,len(wiersz)+1):
        if cyfra % 2 == 0:
            suma_p += int(wiersz[cyfra-1])
        else:
            suma_n += int(wiersz[cyfra-1])
    linia = str(suma_p)+" "+str(suma_n)+"\n"
    zapis.write(linia)
