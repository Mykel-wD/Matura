file = open("dane/napisy.txt", 'r')
dane = file.read().splitlines()

haslo = ""
stop = False
for wiersz in dane:
    cyfry = []
    for znak in wiersz:
        if znak.isdigit():
            cyfry.append(znak)
    if len(cyfry) % 2 != 0:
        cyfry.pop()
    for i in range(0, len(cyfry), 2):
        wartosc = int(cyfry[i] + cyfry[i + 1])
        if 65 <= wartosc <= 90:
            haslo += chr(wartosc)
            koniec = haslo[len(haslo) - 3:len(haslo)]
            if  koniec == "XXX":
                stop = True
    if stop:
        break
print(haslo)
