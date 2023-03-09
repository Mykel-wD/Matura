liczby = list(map(int, open("dane/liczby.txt", 'r').read().splitlines()))
pierwsze = []  # list(map(int, open("dane/pierwsze.txt", 'r').read().splitlines()))

def prime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True
for liczba in liczby:
    if 100 <= liczba <= 5000:
        if prime(liczba):
            print(liczba)
