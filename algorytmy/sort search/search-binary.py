import random

table = []
for i in range(1000000):
    table.append(random.randint(1, 100000))
table.sort()
print(table)


def search(cel, t):
    l = 0
    p = len(t) - 1
    while l <= p:
        mid = (l + p) // 2
        if t[mid] == cel:
            return mid
        else:
            if cel < t[mid]:
                p = mid - 1
            else:
                l = mid + 1
    return "Nie ma"


target = 10
print("index: ", search(target, table))
