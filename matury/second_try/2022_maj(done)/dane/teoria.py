n = 5
ile = 0
t = ['start',2,2,2,2,2]
for i in range(1,n+1):
    if t[i] > n:
        ile = ile + 1
    else:
        liczb = 0
        for j in range(1,n+1):
            if t[j] == i:
                liczb = liczb + 1
        if liczb > 1:
            ile = ile + liczb - 1
print(ile)