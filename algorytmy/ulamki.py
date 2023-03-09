cos = 1

"""
7/2 + 4/5 = 43/10
"""
licznik1 = 7
mianownik1 = 2
licznik2 = 4
mianownik2 = 5

"""
Nieoptymalnie lecz prosto (bez nwd itp, mianownik pewny z mnożenia niż Najwieksza wspólna wielokrotnosc)
"""
def dodaj(l1, m1, l2, m2):
    mianownik = m1 * m2
    l1 *= m2
    l2 *= m1
    licznik = l1 + l2
    return [licznik, mianownik]
"""
dodaj(licznik1, mianownik1, licznik2...):
    nww = nww(mianownik1 , mianownik2) #największa wspólna wielokrotnosc mianownikow
    licznik1 *= nww/mianownik2
    licznik2 *= nww/mianownik1
    licznik = licznik1 + liczik2
    mianownik = nww
    
skroc(licznik, mianownik):
    nwd = nwd(licznik,mianownik)
    licznik /= nwd
    mianownik /= nwd
"""
ulamek_dodany = dodaj(licznik1, mianownik1, licznik2, mianownik2)
print(ulamek_dodany[0], "/", ulamek_dodany[1])
