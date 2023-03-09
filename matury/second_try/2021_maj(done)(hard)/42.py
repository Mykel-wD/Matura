file = open("instrukcje.txt", 'r')
dane = file.read().splitlines()

m_ile = 0
m_cmd = ""
ile = 1

for i in range(len(dane)-1):
    cmd = (dane[i].split(" "))[0]
    cmd2 = (dane[i+1].split(" "))[0]
    if cmd == cmd2:
        ile += 1
    else:
        if ile > m_ile:
            m_ile = ile
            m_cmd = cmd
        ile = 1
print(m_cmd, m_ile)

