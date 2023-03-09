import random

table = []
for i in range(10**4):
    table.append(random.randint(1,10**6))

print(table)
key = 0
for ile in range(len(table)):
    i = ile
    for i in range(ile, len(table)):
        if table[i] < table[key]:
            key = i
    temp = table[ile]
    table[ile] = table[key]
    table[key] = temp
print(table)
