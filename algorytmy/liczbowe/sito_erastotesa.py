
liczby = [0,0]
zakres = 101
for i in range(2,zakres):
    liczby.append(1)

"""
tablica wypelniona 1
gdzie nie bedzie prime to dajemy na 0 
"""
i = 2
while i*i < zakres:
    if liczby[i] == 1: #jesli nie zostala skreslona (jako wielokrotnosc poprzednich liczby)
        for j in range(i*i,zakres,i): #skreslenie wszystkich wielokrotności liczby
            liczby[j] = 0
    i += 1
for i in range(len(liczby)):
    if liczby[i] == 1:
        print(i)


