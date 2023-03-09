
liczba = 220

dzielnik = 2

while liczba > 1:
    if liczba % dzielnik == 0:
        liczba //= dzielnik
        print(dzielnik)
    else:
        dzielnik += 1

