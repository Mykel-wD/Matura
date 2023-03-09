file = open("dane/identyfikator.txt", 'r')
dane = file.read().splitlines()



for wiersz in dane:
    suma = 0
    suma += (ord(wiersz[0]) - 55) * 7
    suma += (ord(wiersz[1]) - 55) * 3
    suma += (ord(wiersz[2]) - 55) * 1
    suma += int(wiersz[4]) * 7
    suma += int(wiersz[5]) * 3
    suma += int(wiersz[6]) * 1
    suma += int(wiersz[7]) * 7
    suma += int(wiersz[8]) * 3
    r = suma % 10
    if r != int(wiersz[3]):
        print(wiersz)
