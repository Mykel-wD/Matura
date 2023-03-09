file = open("dane_PR/dziennik.txt", 'r')
dane = file.read().splitlines()
ciag = 1
ile = 0
kolejny = True
for wiersz in range(1,len(dane)):
    if int(dane[wiersz]) > int(dane[wiersz - 1]):
        ciag += 1
    else:
        ciag = 1
        kolejny = True
    if ciag > 3 and kolejny:
        ile += 1
        kolejny = False
print(ile)
