file = open("dane_pr/sygnaly.txt", 'r')
dane = file.read().splitlines()

for wiersz in dane:
    dobre = True
    for litera in wiersz:
        for litera2 in wiersz:
            if abs(ord(litera)-ord(litera2)) > 10:
                dobre = False
                break
        if not dobre:
            break
    if dobre:
        print(wiersz)
