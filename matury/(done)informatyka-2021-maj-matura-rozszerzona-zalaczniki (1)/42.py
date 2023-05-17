file = open('dane_2105/instrukcje.txt', 'r')
dane = file.read().splitlines()
instrukcje = []
for wiersz in dane:
    instrukcje.append(wiersz.split(" ")[0])
max_ins = ''
max_ile = 0


ile = 1
for i in range(len(instrukcje)-1):
    t = instrukcje[i]
    t2 = instrukcje[i+1]
    if instrukcje[i] == instrukcje[i+1]:
        ile += 1
    else:
        if ile > max_ile:
            max_ile = ile
            max_ins = instrukcje[i]
        ile = 1
print(max_ins, max_ile)