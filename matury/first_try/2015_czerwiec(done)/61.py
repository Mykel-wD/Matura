file = open("dane/kody.txt", "r")
dane = file.read().splitlines()

cyfry = [[0, 10101110111010],
         [1, 11101010101110],
         [2, 10111010101110],
         [3, 11101110101010],
         [4, 10101110101110],
         [5, 11101011101010],
         [6, 10111011101010],
         [7, 10101011101110],
         [8, 11101010111010],
         [9, 10111010111010]]

for wiersz in dane:
    kod = "11011010"
    for znak in wiersz:
        for cyfra in cyfry:
            if znak == str(cyfra[0]):
                kod+=str(cyfra[1])
                break
    liczby = wiersz[::-1]
    liczby2 =[]
    for l in liczby:
        liczby2.append(int(l))
    suma = 0
    for ip in range(0,len(wiersz),2):
        suma += liczby2[ip]
    suma *= 3
    suma2 = 0
    for ip in range(0,len(wiersz)):
        if ip % 2 == 1:
            suma2 += liczby2[ip]
    suma += suma2
    reszta = suma % 10
    reszta = 10 - reszta
    reszta = reszta % 10
    for cyfra in cyfry:
        if reszta == cyfra[0]:
            kod += str(cyfra[1])
            break
    kod += "11010110"
    print(suma, " ",suma2)
