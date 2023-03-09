
liczba = 64
system = 2

wynik = ""
while liczba > 0:
    reszta = liczba % system
    wynik = str(reszta) + wynik
    liczba = liczba // system
print(wynik)

