dane = list(map(int,open("dane4.txt", 'r').read().splitlines()))
m_reg = []
for i in range(0, len(dane)-1):
    reg = []
    luka = abs(dane[i]-dane[i+1])
    reg.append(luka)
    reg.append(dane[i])
    for j in range(i, len(dane) - 1):
        if abs(dane[j] - dane[j+1]) == luka:
            reg.append(dane[j+1])
        else:
            break
    if len(reg) > len(m_reg):
        m_reg = []
        m_reg.extend(reg)
print(m_reg)
print(len(m_reg)-1)