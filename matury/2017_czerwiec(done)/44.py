import math

file = open("dane/punkty.txt", 'r')
dane = file.read().splitlines()


a = 0
b = 0
c = 0

for wiersz in dane:
    kord = wiersz.split(" ")
    x = int(kord[0])
    y = int(kord[1])
    if (x == -5000 and 5000 >= y >= -5000) or (x == 5000 and 5000 >= y >= -5000) or (y == 5000 and 5000 >= x >= -5000) or (y == -5000 and 5000 >= x >= -5000):
        b += 1
    elif 5000 > x > -5000 and 5000 > y > -5000:
        a += 1
    else:
        c += 1
print("a: ", a)
print("b: ", b)
print("c: ", c)