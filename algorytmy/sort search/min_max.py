
zbior = [1,5,2,8,5,-10,120,-1,0,14]
l_min = zbior[0]
l_max = zbior[0]
for liczba in zbior:
    if liczba < l_min:
        l_min = liczba
    if liczba > l_max:
        l_max = liczba
print("min: ",l_min, " max: ", l_max)
