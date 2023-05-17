file = open("dane/kody.txt")
dane = file.read().splitlines()
zapis = open("kody3.txt", "a")
kody = open("dane/cyfra_kodkreskowy.txt", 'r')
cyfry = kody.read().splitlines()

for wiersz in dane:
    linia = "11011010"
    for znak in wiersz:
        linia += (cyfry[int(znak)+1].split("\t"))[1]
    suma_p = 0
    suma_n = 0
    for cyfra in range(1, len(wiersz) + 1):
        if cyfra % 2 == 0:
            suma_p += int(wiersz[cyfra - 1])
        else:
            suma_n += int(wiersz[cyfra - 1])
    suma_p = suma_p * 3
    suma = suma_p + suma_n
    reszta = suma % 10
    kontrolna = 10 - reszta
    kontrolna = kontrolna % 10
    kontrolna = cyfry[kontrolna+1]
    kontrolna = kontrolna.split("\t")
    kontrolna = kontrolna[1]
    linia += kontrolna
    linia += "11010110"
    zapis.write(linia+"\n")
