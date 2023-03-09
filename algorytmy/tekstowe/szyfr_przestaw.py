
slowo = "angel"
slowo = list(slowo) #daje ['A', 'N', 'G'..]
def szyfr(tekst):
    for i in range(0,len(tekst) - 1,2):
        temp = tekst[i]
        tekst[i] = tekst[i + 1]
        tekst[i + 1] = temp
    return tekst
#kod = 'naegl' jesli szyfr(kod) to otrzymamy pierwotny slowo: 'angel'
kod = szyfr(slowo)
print(kod)
print(szyfr(kod))
