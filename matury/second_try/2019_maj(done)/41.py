r = open("dane/liczby.txt", 'r')
dane = r.read().splitlines()
ile = 0

trojki = []
for i in range(12):
    trojki.append(3**i)
print(trojki)
for n in dane:
    if int(n) in trojki:
        ile += 1
print(ile)