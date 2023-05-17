file = open('dane/napisy.txt', 'r')
dane = file.read().splitlines()

haslo = ''
for wiersz in dane:
    x = 'x'
    for znak in wiersz:
        if znak.isdigit():
            if x == 'x':
                x = znak
            else:
                para = int(x + znak)
                if 91 > para > 64:
                    haslo += chr(para)
                x = 'x'
                test = haslo[len(haslo)-3:len(haslo)]
                if test == "XXX":
                    print(haslo)
