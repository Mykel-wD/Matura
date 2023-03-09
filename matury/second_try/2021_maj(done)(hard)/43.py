file = open("instrukcje.txt", 'r')
dane = file.read().splitlines()


literki = []
for wiersz in dane:
    cmd = wiersz.split(" ")
    if cmd[0] == "DOPISZ":
        literki.append(cmd[1])
ile = 0
lit = ""
for l in literki:
    if literki.count(l) > ile:
        ile = literki.count(l)
        lit = l
print(lit, ile)

