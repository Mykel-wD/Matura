linia = True
"""
fib(n) = fib(n-1) + fib(n-2) | fib(5) = fib(4) + fib(3) 'logika'
"""
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)
print(fib(6)) # 3,5,8 | 3+5 = 8
