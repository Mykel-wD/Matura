file = open("dane_pr/sygnaly.txt", 'r')
dane = file.read().splitlines()


ilosci = []
for wiersz in dane:
    rozne = []
    for litera in wiersz:
        if litera not in rozne:
            rozne.append(litera)
    ilosci.append(len(rozne))
liczba = max(ilosci)
print(dane[ilosci.index(liczba)], liczba)