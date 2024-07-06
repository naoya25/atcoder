def main():
    n, k = map(int, input().split())
    m = 998244353

    base2 = 2 * pow(n * n, -1, m)
    base1 = (1 - base2 * (n - 1)) % m

    p1, p2 = 1, 0
    for _ in range(k):
        np1 = p1 * base1 + p2 * base2 * (n - 1)
        np2 = ((1 - np1) * pow(n - 1, -1, m)) % m
        p1, p2 = np1, np2

    ans = (p1 * 1 + p2 * (n * (n + 1) * pow(2, -1, m) - 1)) % m
    # print(p1, p2)
    print(ans)

    return


if __name__ == "__main__":
    main()
