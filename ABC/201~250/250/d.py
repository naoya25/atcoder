# n = int(input())

# def is_prime(num):
#     if num == 2:
#         return True
#     if num % 2 == 0 or num <= 1:
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True


from math import ceil, sqrt


def eratosthenes(n):
    hurui = [i for i in range(n + 1)]
    for i in range(2, ceil(sqrt(n)) + 1):
        for j in range(2, ceil(sqrt(i)) + 1):
            if i == 2:
                continue
            if i % j == 0:
                break
        else:
            for k in range(i + i, n, i):
                if hurui[k] != k:
                    continue
                hurui[k] = 0
        continue
    return hurui


N = int(input())

# 1 <= N <= 10^18
# 10^18以下の250に似た数の素因数は10^6以下
# 10^6以下の素数は何個ある？
# 78499個
# 二乗オーダーの全探索ができそう
# 二分探索でもよい
hurui = eratosthenes(10**6)
primes = [i for i in hurui if i != 0][1:]
ans = 0
for i in range(len(primes) - 1):
    if primes[i] * primes[i + 1] * primes[i + 1] * primes[i + 1] > N:
        break
    ok = i + 1
    ng = len(primes)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if primes[i] * primes[mid] * primes[mid] * primes[mid] <= N:
            ok = mid
        else:
            ng = mid
    ans += ok - i
print(ans)
