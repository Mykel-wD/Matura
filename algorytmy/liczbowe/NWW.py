linia = True

"""
NAJMNIEJSZA WSPÓLNA WIELOKROTNOŚĆ - NWW
NWW(a,b) = a*b / NWD(a,b)
"""
x = 24
y = 16
def nwd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def nww(a, b):
    ab = a * b
    return ab / nwd(a, b)

print("NWW: ",nww(x,y))
