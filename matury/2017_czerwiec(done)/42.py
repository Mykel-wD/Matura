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
    tak = True
    kord = wiersz.split(" ")
    x = kord[0]
    y = kord[1]
    for cyfra in x:
        if cyfra not in y:
            tak = False
    for cyfra in y:
        if cyfra not in x:
            tak = False
    if tak:
        ile += 1
print(ile)