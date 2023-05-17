odczyt = open("dane/liczby.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()
ile2 = 0
for wiersz in dane:
    if wiersz[len(wiersz) - 1] == '2':
        l = wiersz[0:len(wiersz)-1]
        liczba = int(l,2)
        if liczba % 2 == 0:
            ile2 += 1
print(ile2)