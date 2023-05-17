file = open("dane/identyfikator.txt", 'r')
dane = file.read().splitlines()


def poprawne(ids):
    suma = (ord(ids[0]) - 55) * 7
    suma += (ord(ids[1]) - 55) * 3
    suma += (ord(ids[2]) - 55) * 1
    suma += int(ids[4]) * 7
    suma += int(ids[5]) * 3
    suma += int(ids[6]) * 1
    suma += int(ids[7]) * 7
    suma += int(ids[8]) * 3
    k = int(ids[3])
    if suma % 10 == k:
        return True
    return False

poprawne("CIS459437")
for wiersz in dane:
    if not poprawne(wiersz):
        print(wiersz)

file.close()
