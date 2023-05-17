file = open("dane/liczby.txt", 'r')
dane = file.read().splitlines()
file.close()
trojek = 0
piatek = 0
dane = list(map(int, dane))
for x in dane:
    trojka = [x,0,0,0,0]
    for y in dane:
        if y % x == 0 and y not in trojka:
            trojka[1] = y
            for z in dane:
                if z % y == 0 and z not in trojka:
                    trojka[2] = z
                    trojek += 1
                    print(trojka[0],trojka[1],trojka[2])
                    for u in dane:
                        if u % z == 0 and u not in trojka:
                            trojka[3] = u
                            for w in dane:
                                if w % u == 0 and w not in trojka:
                                    trojka[4] = w
                                    piatek += 1
                            trojka[4] = 0
                    trojka[3] = 0
            trojka[2] = 0
    trojka[1] = 0

print("a)\ntrojek: ", trojek)
print("b)\n piatek: ", piatek)