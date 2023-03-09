pierwsze = open("dane/pierwsze.txt", 'r').read().splitlines()


def waga(n):
    n = str(n)
    suma = 0
    if len(n) > 1:
        for cyfra in n:
            suma += int(cyfra)
        return waga(suma)
    else:
        return int(n)


ile = 0
for liczba in pierwsze:
    if waga(int(liczba)) == 1:
        ile += 1
print(ile)
