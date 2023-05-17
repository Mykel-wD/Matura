file = open("liczby.txt", 'r')
liczby = file.read().splitlines()
file.close()
file = open("pierwsze.txt", 'r')
pierwsze = file.read().splitlines()
file.close()

print("zad 1")
def prime(n):
    for i in range(2,n):
        if n % i == 0 :
            return False
    return True
for wiersz in liczby:
    if 100 <= int(wiersz) <= 5000:
        if prime(int(wiersz)):
            print(wiersz)
print("zad 2")
for wiersz in pierwsze:
    if prime(int(wiersz[::-1])):
        print(wiersz)
print("zad 3'\n")
ile = 0
for wiersz in pierwsze:
    n = int(wiersz)
    while int(n) >= 10:
        suma = 0
        n = str(n)
        for znak in n:
            suma += int(znak)
        n = suma
    if n == 1:
        ile += 1
print(ile)
