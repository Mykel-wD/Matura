aa = 23
bb = 13
'''
obliczenie postaci x*a + y*b przy użyciu rekurencji nwd
'''
def nwd(a, b):
    r = a % b
    if r == 0:
        return 0, b
    xp, yp = nwd(b, r)
    x = yp
    y = xp - (a // b * yp)
    return x, y


print(nwd(aa, bb))
