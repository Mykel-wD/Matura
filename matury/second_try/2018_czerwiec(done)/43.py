f = open('dane/dane1.txt', 'r')
dane1 = f.read().splitlines()
f = open('dane/dane2.txt', 'r')
dane2 = f.read().splitlines()
f.close()
for wiersz in range(len(dane1)):
    tak = True
    w1 = list(map(int,dane1[wiersz].split(" ")))
    w2 = list(map(int,dane2[wiersz].split(" ")))
    rozne = []
    for l in w1:
        rozne.append(l)
    for l in w2:
        if l not in rozne:
            tak = False
    rozne = []
    for l in w2:
        rozne.append(l)
    for l in w1:
        if l not in rozne:
            tak = False
    if tak:
        print(wiersz+1)
