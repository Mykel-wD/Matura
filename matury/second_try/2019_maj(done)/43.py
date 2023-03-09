r = open("dane/liczby.txt", 'r')
dane = r.read().splitlines()


def nwd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a = a%b
        else:
            b = b%a
    return a+b

ciagi = []
for i in range(len(dane)):
    a = dane[i]
    ciag = [a,a]
    for j in range(i+1, len(dane)):
        b = dane[j]
        nd= nwd(int(ciag[0]),int(b))
        if nd > 1:
            ciag[0] = nd
            ciag.append(b)
        else:
            ciagi.append(ciag)
            break
dl = []
for ciag in ciagi:
    dl.append(len(ciag))
mi = dl.index(max(dl))
najdl = ciagi[mi]
print(najdl[1], len(najdl)-1, najdl[0])