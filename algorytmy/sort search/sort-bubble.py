
tab = [1,6,2,8,165,34,16,18,21,4,6]
n = len(tab)
for i in range(0,n):
    for j in range(0,n-i-1):
        if tab[j] > tab[j+1]:
            temp = tab[j+1] #swap
            tab[j+1] = tab[j] #swap
            tab[j] = temp #swap
print(tab)

