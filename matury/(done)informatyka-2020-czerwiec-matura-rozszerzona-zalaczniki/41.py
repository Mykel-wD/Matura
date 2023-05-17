file = open("dane_PR2/pary.txt", 'r')
dane = file.read().splitlines()

primes = []
#generacja tablicy liczb pierwszych
def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for i in range(3, 101):
    if prime(i):
        primes.append(i)
print(primes)

for wiersz in dane:
    n = int(wiersz.split(" ")[0])
    if n > 4 and n % 2 == 0:
        stop = False
        for dz1 in primes:
            for dz2 in primes[::-1]:
                if dz1 + dz2 == n:
                    print(n, dz1, dz2)
                    stop = True
                    break
            if stop:
                break
