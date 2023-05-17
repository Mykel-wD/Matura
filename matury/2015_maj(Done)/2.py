file = open("dane_pr/liczby.txt", 'r')
dane = file.read().splitlines()
ile2 = 0
ile8 = 0
for wiersz in dane:
    if int(wiersz,2) % 2 == 0:
        ile2 += 1
    if int(wiersz,4) % 8 == 0:
        ile8 += 1
print(ile2)
print(ile8)