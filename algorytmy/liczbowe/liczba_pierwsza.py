
def prime(liczba):
    i = 2
    while i*i < liczba:
        if liczba % i == 0:
            return False
        i += 1
    return True
print(prime(17))

