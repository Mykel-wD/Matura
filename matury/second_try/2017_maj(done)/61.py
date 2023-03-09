file = open("dane_pr/dane.txt", 'r')
dane = file.read().splitlines()
file.close()
piksele = []
for wiersz in dane:
    linia = wiersz.split(" ")
    piksele.append(linia)
ile = 0

def roznica(a,b):
    if abs(int(a)-int(b)) > 128:
        return True
    return False
sosiad = [[-1,0],[0,1],[1,0],[0,-1]]
for y in range(200):
    for x in range(320):
        kontrast = False
        for s in sosiad:
            sy = s[0]
            sx = s[1]
            if not (y+sy < 0 or x+sx < 0 or y+sy > 199 or x+sx > 319):
                pix1 = piksele[y][x]
                pix2 = piksele[y+sy][x+sx]
                if roznica(pix1, pix2):
                    kontrast = True
        if kontrast:
            ile += 1
print(ile)
