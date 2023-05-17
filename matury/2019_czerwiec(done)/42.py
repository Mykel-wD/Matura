#liczby = list(map(int, open("dane/liczby.txt", 'r').read().splitlines()))
pierwsze = open("dane/pierwsze.txt", 'r').read().splitlines()

def prime(l):
    n = int(l)
    for i in range(2,n-1):
        if n % i == 0:
            return False
    return True

for liczba in pierwsze:
    if prime(liczba[::-1]):
        print(liczba)

