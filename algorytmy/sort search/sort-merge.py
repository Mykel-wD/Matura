import math
import random

table = []
for i in range(10**6):
    table.append(random.randint(1,10**4))

print(table)
def scal(t1, t2):
    wynik = []
    i1 = 0
    i2 = 0
    for i in range(len(t1) + len(t2)):
        if i1 == len(t1):
            wynik.append(t2[i2])
            i2 += 1
        elif i2 == len(t2):
            wynik.append(t1[i1])
            i1 += 1
        else:
            if t1[i1] < t2[i2]:
                wynik.append(t1[i1])
                i1 += 1
            else:
                wynik.append(t2[i2])
                i2 += 1
    return wynik


def sortuj(t):
    return merge_sort(t, 0, len(t) - 1)


def merge_sort(t, l, r):
    if l == r:
        return [t[l]]
    else:
        mid = math.floor((l + r) / 2)
        lewa = merge_sort(t, l, mid)
        prawa = merge_sort(t, mid + 1, r)
        scalona = scal(lewa, prawa)
        return scalona


nowa = sortuj(table)
print(nowa)
