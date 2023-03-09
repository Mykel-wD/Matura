import math
import random

table = []
for i0 in range(10 ** 6):
    table.append(random.randint(1, 10**4))
print(table)


def quick_sort(t):
    if len(t) < 2:
        return t
    else:
        key = t[len(t) - 1]
        lewa = []
        prawa = []
        for i1 in range(0, len(t) - 1):
            liczba = t[i1]
            if liczba <= key:
                lewa.append(liczba)
            else:
                prawa.append(liczba)
        wynik = quick_sort(lewa)
        wynik.append(key)
        wynik.extend(quick_sort(prawa))
        return wynik


table2 = quick_sort(table)
print(table2)
