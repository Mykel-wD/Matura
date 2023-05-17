file = open("dane_2205/liczby.txt", 'r')
dane = list(map(int, file.read().splitlines()))
trojek = 0
piatek = 0
print(dane)
for u in dane:
    piatka = [u]
    for w in dane:
        if w % u == 0 and w not in piatka:
            piatka.append(w)
            for x in dane:
                if x % w == 0 and x not in piatka:  # trojka
                    piatka.append(x)
                    print(piatka)
                    trojek += 1
                    for y in dane:
                        if y % x == 0 and y not in piatka:
                            piatka.append(y)
                            for z in dane:
                                if z % y == 0 and z not in piatka:  # piatka
                                    piatek += 1
                            piatka.pop(3)
                    piatka.pop(2)
            piatka.pop(1)

print("wynik: ")
print(trojek, "trojek")
print(piatek, "piatek")
