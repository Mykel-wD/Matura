
systemm = 2

l = "1011"
liczba = list(map(int,list(l))) # 1011 jako array: liczba[0..n]
def homer(n, system):
    wynik = 0
    for i in range(len(n)):
        wynik = wynik * system + n[i]
    return wynik

print(homer(liczba, systemm))
