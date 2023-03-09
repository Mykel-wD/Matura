
a = 5
potega = 3

wynik = 1
czynnik = a
while potega > 0:
    bit = potega % 2
    potega //= 2
    if bit == 1:
        wynik *= czynnik
    czynnik *= czynnik
print(wynik)
