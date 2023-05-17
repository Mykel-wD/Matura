odczyt = open("dane/liczby.txt", 'r')
dane = odczyt.read().splitlines()
odczyt.close()
ile4 = 0
for wiersz in dane:
    if wiersz[len(wiersz)-1]=='4':
        if wiersz.count('0')==0:
            ile4 += 1
print(ile4)