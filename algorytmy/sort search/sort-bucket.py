"""INTEGERY"""
tab = [1, 6, 2, 8, 165, 34, 16, 18, 21, 4, 6]
kubly = []
for t in range(max(tab) + 1):  # tablica z max(tab) kublami (1 - 165)
    kubly.append([])

for liczba in tab:
    kubly[liczba].append(liczba)  # porzadkujemy liczba do odpowiadającego kubla

s_tab = []
for kubel in kubly:  # wypisanie pokolei
    for liczba in kubel:
        s_tab.append(liczba)
print(s_tab)

"""FLOATY
(kod poniżej) k = ile kublow. Wkladanie 0,2 do kubla o indexie: podłoga(k*0,2)
"""
tab = [.5, .5, .8, .9, .4, .2, 0.4, 0.1, .9]
k = 4
kubly = []
for t in range(k):  # tablica z k kublami
    kubly.append([])

for liczba in tab: # porzadkujemy liczba do odpowiadającego kubla
    kubel = int(liczba * k)
    kubly[kubel].append(liczba)

s_tab = []
for kubel in kubly:  # wypisanie pokolei
    for liczba in kubel:
        s_tab.append(liczba)
print(s_tab)
