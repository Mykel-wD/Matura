#algorytm sluzy wyznaczeniu miejsca zerowego w okreslonym zakresie
def f(x):
    return x ** 2 - 60
a = 0
b = 10
"""
    Limit wykonywania funkcji:
    przyjmujemy epsilum (taki znak euro E)
    to odleglosc miedzy koncami zakresu (a - b)
    gdy odl < epsilum, wypisz przyblizenie
"""
epsilum = 0.00000000000001
while abs(a - b) > epsilum:
    odl = abs(a - b)
    c = (a + b) / 2
    y = f(c)
    if y == 0:
        print("znaleziono! ", c)
        break
    if y > 0:
        b = c
    else:
        a = c
print("przybliżenie: ", c)
