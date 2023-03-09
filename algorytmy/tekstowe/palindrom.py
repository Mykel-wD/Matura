slowo = "alaa"

n = len(slowo)
i = 0
j = n - 1
czy = True
while i < j:
    if slowo[i] != slowo[j]:
        czy = False
        break
    i += 1
    j -= 1
if czy:
    print(slowo, " to palindrom")
else:
    print("nie")
