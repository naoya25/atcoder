def main():
    n = int(input())
    a = list(map(int, input().split()))
    k = list(map(lambda x: 10 ** len(str(x)), a))
    m = 998244353

    ans = 0
    for i in range(1, n):
        ans += a[-i] * (n - i)

    sum_k = sum(k)
    for i in range(n - 1):
        sum_k -= k[i]
        ans += (sum_k * a[i]) % m

    print(ans % m)


if __name__ == "__main__":
    main()
