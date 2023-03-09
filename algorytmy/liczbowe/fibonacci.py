zakres = 100

a = 1
b = 0
c = 0
while c <= zakres:
    c = a + b
    a = b
    b = c
    print(c)
