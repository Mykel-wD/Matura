sslowo1 = "kam"
sslowo2 = "mak"
n1 = len(sslowo1)
n2 = len(sslowo2)

def anagram(slowo1, slowo2):
    if n1 != n2: #dlugosci rózne
        return False
    else:
        if sorted(slowo1) != sorted(slowo2):
            return False
        return True

print(anagram(sslowo1, sslowo2))

