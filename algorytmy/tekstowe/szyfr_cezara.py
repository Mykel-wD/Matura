tekst = "PrawoGora"

"""
szyfrowanie w prawo więc event 'if litera == 'Z':' jesli w lewo to 'if litera == 'A': wiesz czemu
"""
def szyfr(t, klucz):
    sz = ""
    for znak in t:
        litera = znak
        for i in range(klucz):
            if litera == 'Z':
                litera = 'A'
            elif litera == 'z':
                litera = 'a'
            else:
                litera = chr(ord(litera)+1)
        sz+= litera
    return sz
def deszyfr(t, klucz):
    sz = ""
    for znak in t:
        litera = znak
        for i in range(klucz):
            if litera == 'A':
                litera = 'Z'
            elif litera == 'a':
                litera = 'z'
            else:
                litera = chr(ord(litera) - 1)
        sz += litera
    return sz

kod = szyfr(tekst,2)
print(kod)
print(deszyfr(kod,2))

