dane = list(map(int,open("dane4.txt", 'r').read().splitlines()))

luki = []
for i in range(0, len(dane)-1):
    luka = abs(dane[i]-dane[i+1])
    luki.append(luka)
mluk = 0
for luka in luki:
    ile = luki.count(luka)
    if ile > mluk:
        mluk = ile
print(mluk)
for luka in luki:
    if luki.count(luka) == mluk:
        print(luka)