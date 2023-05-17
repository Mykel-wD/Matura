file = open("dane/punkty.txt", 'r')
dane = file.read().splitlines()

def prime(n):
    if n <= 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

ile = 0
for wiersz in dane:
    kord = wiersz.split(" ")
    x = int(kord[0])
    y = int(kord[1])
    if prime(x) and prime(y):
        ile += 1
print(ile)