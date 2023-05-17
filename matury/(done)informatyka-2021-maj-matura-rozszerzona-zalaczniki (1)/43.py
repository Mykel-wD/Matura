file = open('dane_2105/instrukcje.txt', 'r')
dane = file.read().splitlines()
litery = {}
for wiersz in dane:
    ins, litera = wiersz.split(" ")
    if ins == "DOPISZ":
        if litera in litery:
            litery[litera] += 1
        else:
            litery[litera] = 1
print(litery)
