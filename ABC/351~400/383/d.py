def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def main():
    n = int(input())

    # パターン1: p^8 <= n を満たす素数pを探す
    limit_p8 = int(n ** (1 / 8))

    # パターン2: p^2 * q^2 <= n を満たす素数ペア(p,q)
    limit_sieve = int(n**0.5)
    primes = sieve(limit_sieve)

    count = 0

    # パターン1: p^8 <= n
    for p in primes:
        if p**8 <= n:
            count += 1
        else:
            break

    # パターン2: p^2 q^2 <= n
    plen = len(primes)
    for i in range(plen):
        p = primes[i]
        p2 = p * p
        if p2 * p2 > n:
            break
        max_q = int((n / p2) ** 0.5)
        # 二分探索
        left, right = i + 1, plen - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if primes[mid] <= max_q:
                pos = mid
                left = mid + 1
            else:
                right = mid - 1
        if pos != -1:
            count += pos - (i + 1) + 1

    print(count)


if __name__ == "__main__":
    main()
