import random

table = []
for i in range(10**4):
    table.append(random.randint(1,10**6))

print(table)
for ile in range(1,len(table)):
    key = table[ile]
    for i in range(ile-1, -1, -1):
        if key < table[i]:
            table[i+1] = table[i]
        else:
            table[i+1] = key
            break
        if i == 0:
            table[0] = key
print(table)
