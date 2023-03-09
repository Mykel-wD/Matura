file = open("pary.txt", 'r')
dane = file.read().splitlines()
mliczba = 9999999999
mt = ""
for wiersz in dane:
    t = wiersz.split(" ")[1]
    liczba = int(wiersz.split(" ")[0])
    if liczba == len(t):
        if liczba < mliczba:
            mliczba = liczba
            mt = t
        elif liczba == mliczba:
            if t < mt:
                mt = t
print(mliczba, mt)

