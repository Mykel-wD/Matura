file = open("dane/dane_anagramy.txt", 'w')
file.write("")
file = open("dane/dane_anagramy.txt", 'a')
s = 0
for n in range(1,1000):
    for i in range(1,n+1):
        for j in range(1, n+1):
            s += 1
    linia = str(n)+" "+str(s)+"\n"
    file.write(linia)
