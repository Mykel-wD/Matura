
slowo1 = "kokoa"
slowo2 = "kosok"
if len(slowo1) != len(slowo2):
    print("nie anagram")
n = len(slowo1)
"""
1. Tablica wypełniona zerami np. 200 slotowa
"""
tablica = []
for i in range(200):
    tablica.append(0)
"""
2. zliczenie wystapien ord z liter slowa
"""
for i in range(n): #ord(k) = 70
    tablica[ord(slowo1[i])] += 1 #tablica[70] = 1
"""
2. odjecie wystapien ord z liter slowa2
"""
for i in range(n):
    tablica[ord(slowo2[i])] -= 1
"""
3. Jeśli jakas litera wystapiła różnie to nie anagram
"""
for i in range(200):
    if tablica[i] != 0:
        print("nie anagram")
