file = open("pary.txt", 'r')
dane = file.read().splitlines()

for wiersz in dane:
    t = wiersz.split(" ")[1]
    znak = t[0]
    dl = 1
    mdl = 1
    mznak = t[0]
    for i in range(len(t)-1):
        if t[i+1] == znak:
            dl += 1
        else:
            if dl > mdl:
                mdl = dl
                mznak = znak
            znak = t[i+1]
            dl = 1
    if dl > mdl:
        mdl = dl
        mznak = znak
    print(mznak*mdl, mdl)
