import time
import math

def rabbit(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return rabbit(n - 1) + rabbit(n - 2)


t1 = time.perf_counter()


def fibo(n, m):
    fib = [0] * (n + 1)
    fib[0] = 1
    fib[1] = 1
    fib[2] = 1

    if m == 1:
        return 0
    elif m == 2:
        return 1
    else:
        for i in range(3, m + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        for j in range(n - m):
            fib[m + 1 + j] = fib[m + j] + fib[m - 1 + j] - fib[j]
        return fib[n]


print(fibo(89, 16))

def lis(n):
    ll = [[] for i in range(len(n))]




t2 = time.perf_counter()
print(t2 - t1)
