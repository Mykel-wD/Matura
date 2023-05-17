#ok
zbior = [1,2,2,3,3,3,3,2,3]
zbior_kopia = []
for l in zbior: # zbior2 = zbior bedzie zmieniac wartosci w obu listach
    zbior_kopia.append(l)
n = len(zbior)
"""
Lider - wystepuje w zbiorze polowe+1 razy (np. 4 trójki w 7 el zbiorze)
"""
while len(zbior) > 1:
    liczba1 = zbior[0]
    zbior.pop(zbior.index(liczba1))
    for i in range(0,len(zbior)):
        if zbior[i] != liczba1:
            liczba2 = zbior[i]
            zbior.pop(zbior.index(liczba2))
            break
if len(zbior) > 0:
    pozostala = zbior[0]
    if zbior_kopia.count(pozostala) > n//2: #ilosc liczby w poczatkowym zbiorze
        print(pozostala)
print(int("5F",16))
