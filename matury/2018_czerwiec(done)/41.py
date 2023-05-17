f = open('dane/dane1.txt', 'r')
dane1 = f.read().splitlines()
f = open('dane/dane2.txt', 'r')
dane2 = f.read().splitlines()
f.close()
ile = 0
for wiersz in range(len(dane1)):
    w1 = dane1[wiersz].split(" ")
    w2 = dane2[wiersz].split(" ")
    if w1[9] == w2[9]:
        ile += 1
print(ile)