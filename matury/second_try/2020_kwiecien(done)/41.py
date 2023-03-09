dane = list(map(int,open("dane4.txt", 'r').read().splitlines()))
luki = []
for i in range(0, len(dane)-1):
    luka = abs(dane[i]-dane[i+1])
    luki.append(luka)
print("min", min(luki))
print("max", max(luki))