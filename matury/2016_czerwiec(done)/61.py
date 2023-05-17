odczyt = open("dane/liczby.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()
ile8 = 0
for wiersz in dane:
    if wiersz[len(wiersz)-1]=='8':
        ile8 += 1
print(ile8)