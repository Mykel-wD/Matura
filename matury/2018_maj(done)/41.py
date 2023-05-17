file = open("dane_pr/sygnaly.txt", 'r')
dane = file.read().splitlines()

haslo = ''
for i in range(39, len(dane), 40):
    haslo += dane[i][9]
print(haslo)