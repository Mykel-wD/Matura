slowo = "ala"
n = len(slowo)
wzor = "ala"
n2= len(wzor)

ile = 0
koniec = n-n2+1 #koniec iteracji 3 znaki od konca (bo taki wzor)
if n < n2:  #jesli wzorzec tak dlugi jak slowo w ktorym szukamy to sprawdzamy
    print("nie ma")
else:
    for i in range(0, koniec):
        jest = True
        for j in range(0, n2): #j = indeksy wzoru
            if slowo[i+j] != wzor[j]:
                jest = False
                break
        if jest:
            ile += 1
    print(ile)
