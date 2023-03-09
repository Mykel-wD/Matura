
pierwiastek_z = 3
eps = 0.001 #epsilum dokladnosci
a = 3 # pierwsiatek szukany
b = 1
while abs(a-b) >  eps:
    a = (a+b) / 2
    b = pierwiastek_z / a
print(a)
