file = open("dane_PR2/pary.txt", 'r')
dane = file.read().splitlines()

for wiersz in dane:
    slowo = wiersz.split(" ")[1]
    max_dl = 0
    max_znak = ''
    dl = 1
    znak = slowo[0]
    for i in range(len(slowo)-1):
        if slowo[i] == slowo[i+1]:
            dl += 1
        else:
            if dl > max_dl:
                max_znak = znak
                max_dl = dl
            dl = 1
            znak = slowo[i+1]
    if dl > max_dl:
        max_znak = znak
        max_dl = dl
    print(max_znak*max_dl, max_dl)