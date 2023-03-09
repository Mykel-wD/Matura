f = open('dane/dane1.txt', 'r')
dane1 = f.read().splitlines()
f = open('dane/dane2.txt', 'r')
dane2 = f.read().splitlines()
f.close()
ile = 0
for wiersz in range(len(dane1)):
    w1 = dane1[wiersz].split(" ")
    w2 = dane2[wiersz].split(" ")
    p1 = 0
    p2 = 0
    for i in range(10):
        if int(w1[i]) % 2 == 0:
            p1 += 1
        if int(w2[i]) % 2 == 0:
            p2 += 1
    if p1 == p2 == 5:
        ile += 1

print(ile)