
liczba = 64
system = 2

wynik = ""
def convert(n,sys):
    if n == 0:
        return
    global wynik
    reszta = n % sys
    wynik = str(reszta) + wynik
    convert(n//sys,sys)

convert(64,2)
print(wynik)

