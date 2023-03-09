
liczba = 40
system = 16

wynik = 0
czynnik = 0
while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    # Start
    wynik += cyfra * system ** czynnik
    czynnik += 1
    #koniec
print(wynik)

