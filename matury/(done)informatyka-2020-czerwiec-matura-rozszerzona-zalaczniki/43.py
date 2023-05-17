file = open("dane_PR2/pary.txt", 'r')
dane = file.read().splitlines()

pary = []
for wiersz in dane:
    n,slowo = wiersz.split(" ")
    if int(n) == len(slowo):
        pary.append([int(n), slowo])
print(pary)
print(min(pary))
min_n = pary[0][0]
for para in pary:
    if para[0] < min_n:
        min_n = para[0]
min_z = 'zzzzzzzzz'
for para in pary:
    if para[0] == min_n:
        if para[1] < min_z:
            min_z = para[1]
print(min_n, min_z)
