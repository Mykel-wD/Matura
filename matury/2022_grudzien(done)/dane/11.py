file = open("liczby.txt", 'r')
dane = file.read().splitlines()


def prime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

min_r = 99999999999
min_l = 0
max_r = 0
max_l = 0
znacznik = 1
for wiersz in dane:
    n = int(wiersz)
    dl = 0
    for dz1 in range(2, n//2+1):
        if prime(dz1):
            dz2 = n-dz1
            if prime(dz2):
                dl += 1
    if dl > max_r:
        max_l = wiersz
        max_r = dl
    if dl < min_r:
        min_l = wiersz
        min_r = dl
    print(znacznik)
    znacznik += 1
print(max_l, max_r, min_l, min_r)
print(prime(11))