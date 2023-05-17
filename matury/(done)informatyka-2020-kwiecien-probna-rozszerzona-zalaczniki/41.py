file = open("dane4.txt", "r")
dane = list(map(int, file.read().splitlines()))
file.close()

luki = []
luki_r = {}
for i in range(len(dane) - 1):
    luki.append(abs(dane[i] - dane[i + 1]))
for luka in luki:
    if luka not in luki_r.keys():
        luki_r[luka] = 1
    else:
        luki_r[luka] += 1
max_krot = max(luki_r.values())
for luka in luki_r.items():
    if luka[1] == max_krot:
        print(luka[0])