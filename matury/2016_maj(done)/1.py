import math

file = open("dane/punkty.txt", "r")
dane = file.read().splitlines()
kolo = 0

for wiersz in dane:
    coords = wiersz.split(" ")
    x = int(coords[0])
    y = int(coords[1])
    od_srodka = math.sqrt((200 - x) ** 2 + (200 - y) ** 2)
    if od_srodka == 200:
        print(wiersz)
    elif od_srodka < 200:
        kolo += 1
print("kolo: ", kolo)
