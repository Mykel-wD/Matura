import math

file = open("liczby.txt", 'r')
dane = file.read().splitlines()
file.close()
dane = list(map(int,dane))
def nwd(a,b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

w1 = dane[0]
dl = 0
p = 0
dz = 0
max_dl = 0
max_p = 0
max_dz = 0

for i in range(len(dane)-1):
    w2 = dane[i+1]
    if nwd(w1,w2) > 1:
        dz = nwd(w1,w2)
        w1 = dz
    else:
        if dl > max_dl:
            max_dl = dl
            max_dz = dz
            max_p = p
        dl = 1
        p = w2

