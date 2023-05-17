file = open("dane/liczby.txt", 'r')
dane = file.read().splitlines()
file.close()
ile = 0
zapis = True
slowo = ""
for wiersz in dane:
    if wiersz[0] == wiersz[len(wiersz)-1]:
        if zapis:
            slowo = wiersz
            zapis = False
        ile += 1
print(ile,slowo)
