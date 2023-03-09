file = open("dane/identyfikator.txt", 'r')
dane = file.read().splitlines()


def pal(s):
    if s == s[::-1]:
        return True
    return False


for wiersz in dane:
    if pal(wiersz[0:3]) or pal(wiersz[3:9]):
        print(wiersz)

