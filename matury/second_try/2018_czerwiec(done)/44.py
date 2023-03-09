f = open('dane/dane1.txt', 'r')
dane1 = f.read().splitlines()
f = open('dane/dane2.txt', 'r')
dane2 = f.read().splitlines()
f.close()
wynik = open("wynik4_4.txt", 'w')
wynik.write("")
wynik = open("wynik4_4.txt", 'a')
for wiersz in range(len(dane1)):
    w1 = list(map(int,dane1[wiersz].split(" ")))
    w2 = list(map(int,dane2[wiersz].split(" ")))
    w1.extend(w2)
    ws = ""
    w2 = sorted(w1)
    for l in w2:
        ws += str(l)+" "
    ws += "\n"
    wynik.write(ws)
wynik.close()
