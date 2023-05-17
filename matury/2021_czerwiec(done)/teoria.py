def dlug(n):
    dl = 0
    while n > 0:
        for dz in range(1,n):
            if dz*dz <= n:
                dzielnik = dz*dz
            else:
                break
        n = n-dzielnik
        dl = dl + 1
    return dl
print(dlug(32))