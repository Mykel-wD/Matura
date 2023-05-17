file = open("instrukcje.txt", 'r')
dane = file.read().splitlines()

wynik = []
for wiersz in dane:
    w = wiersz.split(" ")
    litera = w[1]
    cmd = w[0]
    if cmd[0] == "D":
        wynik.append(litera)
    elif cmd[0] == "Z":
        wynik[len(wynik)-1] = litera
    elif cmd[0] == "U":
        wynik.pop()
    else:
        if wynik.count(litera) > 0:
            index = wynik.index(litera)
            if litera == "Z":
                litera = "A"
            else:
                litera = chr(ord(litera)+1)
            wynik[index] = litera
print(len(wynik))