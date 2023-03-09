import math

r = open("dane/liczby.txt", 'r')
dane = r.read().splitlines()

for wiersz in dane:
    suma = 0
    for c in wiersz:
        suma += math.factorial(int(c))
    if suma == int(wiersz):
        print(wiersz)