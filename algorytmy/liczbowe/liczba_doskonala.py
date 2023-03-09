liczba = int(input("podaj liczbe"))

suma = 1
i = 2
while i <= liczba / 2:
    if liczba % i == 0:
        suma += i  # dzielnik pierwszy (27 % dzielnik == 0)
    i += 1
if suma == liczba:
    print("doskonala")

""" Wersja lepsza """

liczba = int(input("podaj liczbe"))

suma = 1
i = 2
while i * i <= liczba:
    if i * i == liczba:
        suma += i
    else:
        if liczba % i == 0:
            suma += i  # dzielnik pierwszy (27 % dzielnik == 0)
            suma += liczba / i  # drugi dzielnik (27 / dzielnik = dzielnik2)
        i += 1
if suma == liczba:
    print("doskonala")
