s = "MA_FOYKARZNRTITU_IMA_"
n = len(s)
k = 3
t = []
kolumn = int(n / k)
wierszy = k
tablica = []
for i in range(wierszy):
    tablica.append([])
    for j in range(kolumn):
        tablica[i].append([])

znak = 0
for w in range(wierszy):
    for kol in range(kolumn):
        tablica[w][kol].append(s[znak])
        znak += 1
for tab in tablica:
    print(tab)
for kol in range(kolumn):
    if kol % 2 == 0:
        for w in range(wierszy):
            t.append(tablica[w][kol])
    else:
        for w in range(wierszy-1,-1,-1):
            t.append(tablica[w][kol])
print(t)