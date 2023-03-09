A = [1000,6,8,11,15,20,35,70,100,3]
x = A[0]
n = len(A)
parzyste = True
for i in range(n):
    if A[i] % 2 == 1:
        parzyste = False
        if A[i] < x:
            x = A[i]
    elif parzyste:
        if A[i] > x:
            x = A[i]
print(x)